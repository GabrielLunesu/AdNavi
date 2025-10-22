# Redis Context Manager Architecture

## Overview

The Redis Context Manager provides distributed, persistent conversation history storage for multi-turn QA interactions. It replaces the in-memory implementation to enable horizontal scaling and production-ready session management.

## Why Redis?

**Problem**: The original in-memory `ContextManager` had critical limitations:
- Lost conversation history on server restarts
- Failed with multi-instance deployments (load balancing)
- No automatic cleanup of stale sessions
- Single-process limitation

**Solution**: Redis-backed storage provides:
- ✅ **Multi-instance support**: Shared state across API instances
- ✅ **Persistence**: Survives server restarts
- ✅ **TTL-based cleanup**: Automatic expiration after 1 hour
- ✅ **High performance**: Connection pooling and optimized operations
- ✅ **Production-ready**: Redis is battle-tested for this use case

## Architecture

### Component Overview

```
┌─────────────────┐
│   FastAPI App   │
│  (Multiple      │
│   Instances)    │
└────────┬────────┘
         │
         │ Uses
         ▼
┌─────────────────┐
│ app/state.py    │
│  Singleton      │
│ RedisContext    │
│ Manager         │
└────────┬────────┘
         │
         │ Connection Pool
         ▼
┌─────────────────┐
│     Redis       │
│   (Shared)      │
│  - Context      │
│  - TTL          │
│  - Persistence  │
└─────────────────┘
```

### Key Design Decisions

1. **Fail-Fast Approach**: No fallback to in-memory storage
   - Clear error messages when Redis unavailable
   - Forces proper Redis setup in all environments
   - Prevents silent failures

2. **Connection Pooling**: Reuse connections for performance
   - Configurable pool size (default: 50 connections)
   - Automatic connection management
   - Thread-safe by default

3. **TTL Strategy**: TTL refreshed on every write
   - Keeps active conversations alive
   - Auto-expires abandoned sessions
   - Prevents unbounded memory growth

4. **Key Structure**: Scoped by user+workspace
   - Format: `context:{user_id}:{workspace_id}`
   - Tenant isolation at the data level
   - Easy cleanup and monitoring

## Implementation Details

### Data Structure

**Redis Lists** for FIFO behavior:
- `LPUSH` adds entry to front
- `LTRIM` keeps only last N entries
- `LRANGE` retrieves all entries

**Entry Format** (JSON):
```json
{
  "question": "What's my ROAS?",
  "dsl": {
    "metric": "roas",
    "time_range": {"last_n_days": 7}
  },
  "result": {
    "summary": 2.5,
    "delta_pct": 0.19
  }
}
```

### TTL Behavior

- **Default TTL**: 3600 seconds (1 hour)
- **Refreshed**: On every `add_entry()` call
- **Expiration**: Automatic cleanup by Redis
- **Effect**: Abandoned conversations expire after 1 hour of inactivity

### FIFO Eviction

- **Max History**: 5 entries per user+workspace (configurable)
- **Eviction**: Automatic when limit exceeded
- **Strategy**: FIFO (oldest entries removed first)
- **Effect**: Maintains recent context without unbounded growth

## Configuration

### Environment Variables

```bash
# Redis connection URL
REDIS_URL=redis://localhost:6379/0

# Context configuration
CONTEXT_MAX_HISTORY=5
CONTEXT_TTL_SECONDS=3600
```

### Docker Compose

```yaml
services:
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
```

## Usage

### Basic Operations

```python
from app import state

# Add conversation entry
state.context_manager.add_entry(
    user_id="user123",
    workspace_id="ws456",
    question="What's my ROAS?",
    dsl={"metric": "roas"},
    result={"summary": 2.5}
)

# Retrieve context
context = state.context_manager.get_context("user123", "ws456")

# Clear context
state.context_manager.clear_context("user123", "ws456")
```

### QA Service Integration

The QA service automatically uses Redis for context:

```python
# First question
response1 = qa_service.answer(
    question="What's my ROAS this week?",
    workspace_id="ws123",
    user_id="user456"
)
# Context stored to Redis

# Follow-up question
response2 = qa_service.answer(
    question="And yesterday?",
    workspace_id="ws123",
    user_id="user456"
)
# Context retrieved from Redis to infer "roas" metric
```

## Monitoring & Debugging

### Health Check

```python
# Check Redis connectivity
if state.context_manager.health_check():
    print("Redis is healthy")
else:
    print("Redis is down")
```

### Get All Active Sessions

```python
# List all active conversations
keys = state.context_manager.get_all_keys()
print(f"Active conversations: {len(keys)}")
```

### Redis CLI Debugging

```bash
# Connect to Redis
redis-cli

# List all context keys
KEYS context:*

# View specific context
LRANGE context:user123:ws456 0 -1

# Check TTL
TTL context:user123:ws456

# Monitor commands
MONITOR
```

## Performance Characteristics

### Latency

- **Add Entry**: < 2ms (local Redis)
- **Get Context**: < 1ms (local Redis)
- **Health Check**: < 1ms (ping)

### Capacity

- **Storage**: ~1KB per conversation entry
- **Max Concurrent**: Unlimited (horizontal scaling)
- **Memory**: TTL prevents unbounded growth

### Concurrent Access

- **Thread-Safe**: Yes (Redis handles concurrency)
- **Connection Pool**: 50 connections (configurable)
- **Lock-Free**: No explicit locking needed

## Troubleshooting

### Redis Connection Failed

**Error**: `ConnectionError: Redis unavailable`

**Solutions**:
1. Verify Redis is running: `docker ps | grep redis`
2. Check connection URL: `echo $REDIS_URL`
3. Test connection: `redis-cli ping`
4. Check network: Ensure Redis port accessible

### Context Lost

**Error**: Context empty after restart

**Solutions**:
1. Verify appendonly mode enabled in Redis
2. Check Redis persistence directory
3. Verify TTL hasn't expired
4. Check Redis logs for errors

### Multi-Instance Not Working

**Error**: Context not shared between instances

**Solutions**:
1. Verify both instances use same `REDIS_URL`
2. Check Redis is externally accessible
3. Verify network connectivity between instances
4. Check Redis ACLs/authentication

## Migration from In-Memory

### Timeline

1. **Phase 1**: Deploy Redis alongside application
2. **Phase 2**: Update code to use RedisContextManager
3. **Phase 3**: Test multi-instance behavior
4. **Phase 4**: Remove in-memory implementation

### Breaking Changes

- **Requires Redis**: Application fails to start without Redis
- **No Fallback**: Fail-fast approach, no degradation
- **Configuration**: Must set `REDIS_URL` environment variable

### Data Migration

- **Not Required**: Context is ephemeral (1 hour TTL)
- **Acceptable Loss**: Conversation history resets on deployment
- **User Impact**: Minimal (context already transient)

## Future Enhancements

1. **Context Compression**: Reduce storage for large results
2. **Smart Pruning**: Keep relevant context, not just recent
3. **Cross-Session**: Persist context across user sessions
4. **Analytics**: Track conversation patterns
5. **Cluster Mode**: High availability with Redis Cluster

## Related Files

- `app/context/redis_context_manager.py`: Implementation
- `app/state.py`: Singleton initialization
- `app/services/qa_service.py`: Uses context manager
- `app/nlp/translator.py`: Consumes context for follow-ups
- `compose.yaml`: Redis service configuration
- `app/deps.py`: Settings configuration

## References

- [Redis Documentation](https://redis.io/docs/)
- [Python Redis Client](https://redis-py.readthedocs.io/)
- [Connection Pooling](https://redis.io/docs/manual/scaling/)
- [TTL Patterns](https://redis.io/docs/manual/patterns/time-series/)

