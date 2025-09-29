# AdNavi API Documentation

## Swagger/OpenAPI Documentation

The AdNavi FastAPI backend now includes comprehensive Swagger documentation that is automatically generated from your API endpoints.

### Accessing the Documentation

When the backend server is running, you can access the interactive documentation at:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI JSON Schema**: `http://localhost:8000/openapi.json`

### Features Added

#### 1. Enhanced API Metadata
- **Title**: AdNavi API
- **Version**: 1.0.0
- **Description**: Comprehensive description of the platform and API capabilities
- **Contact Information**: Support email
- **Server URLs**: Development and production server configurations

#### 2. Authentication Documentation
- **Security Scheme**: JWT-based authentication using HTTP-only cookies
- **Cookie Name**: `access_token`
- **Format**: `Bearer <token>`
- **Protected Endpoints**: Automatically documented with security requirements

#### 3. Comprehensive Endpoint Documentation

##### Authentication Endpoints (`/auth`)
- `POST /auth/register` - User registration with workspace creation
- `POST /auth/login` - User authentication with cookie-based session
- `GET /auth/me` - Get current user information
- `POST /auth/logout` - Clear authentication session

##### Workspace Management (`/workspaces`)
- `GET /workspaces/` - List accessible workspaces
- `GET /workspaces/{workspace_id}` - Get workspace details
- `PUT /workspaces/{workspace_id}` - Update workspace information
- `GET /workspaces/{workspace_id}/users` - List workspace users

##### Connection Management (`/connections`)
- `GET /connections/` - List ad platform connections
- `POST /connections/` - Create new ad platform connection
- `GET /connections/{connection_id}` - Get connection details
- `PUT /connections/{connection_id}` - Update connection
- `DELETE /connections/{connection_id}` - Delete connection

##### Entity Management (`/entities`)
- `GET /entities/` - List entities (campaigns, ad sets, ads)
- `POST /entities/` - Create new entity
- `GET /entities/{entity_id}` - Get entity details
- `PUT /entities/{entity_id}` - Update entity
- `DELETE /entities/{entity_id}` - Delete entity
- `GET /entities/{entity_id}/children` - Get child entities

##### Performance Metrics (`/metrics`)
- `GET /metrics/` - List performance metrics
- `GET /metrics/summary` - Get aggregated metrics summary
- `GET /metrics/{metric_id}` - Get specific metric details
- `GET /metrics/entity/{entity_id}/daily` - Get daily metrics for entity

##### P&L Analytics (`/pnl`)
- `GET /pnl/` - List P&L records
- `GET /pnl/summary` - Get P&L summary with aggregations
- `GET /pnl/{pnl_id}` - Get specific P&L record
- `GET /pnl/entity/{entity_id}/daily` - Get daily P&L for entity
- `GET /pnl/compute-runs/` - List compute runs

##### Health Check
- `GET /health` - Service health status

#### 4. Response Models and Examples
All endpoints include:
- **Request schemas** with field descriptions and examples
- **Response models** for successful operations
- **Error response models** with standardized error format
- **Status code documentation** (200, 201, 400, 401, 500)
- **Example payloads** for both requests and responses

#### 5. Security Enhancements
- **Environment Variables**: Admin panel secrets moved to environment configuration
- **Security Warnings**: Alerts when using default secrets in development
- **Production Ready**: Proper secret management for production deployment

### Environment Variables

To properly configure the application, set these environment variables:

```bash
# Required for JWT authentication
JWT_SECRET=your-secret-jwt-key-here

# Optional - defaults to development values
ADMIN_SECRET_KEY=your-admin-panel-secret-key
BACKEND_CORS_ORIGINS=http://localhost:3000
COOKIE_DOMAIN=localhost
```

### Development Usage

1. Start the FastAPI server:
   ```bash
   cd backend
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. Open your browser and navigate to `http://localhost:8000/docs`

3. You'll see the interactive Swagger UI with:
   - All available endpoints
   - Request/response schemas
   - Try-it-out functionality
   - Authentication flow testing

### API Testing with Swagger UI

1. **Register a new user**: Use the `/auth/register` endpoint
2. **Login**: Use the `/auth/login` endpoint (this sets the authentication cookie)
3. **Access protected endpoints**: The cookie is automatically included in subsequent requests
4. **View current user**: Test the `/auth/me` endpoint
5. **Logout**: Clear the session with `/auth/logout`

### Production Considerations

Before deploying to production:

1. Set strong, unique values for `JWT_SECRET` and `ADMIN_SECRET_KEY`
2. Update `BACKEND_CORS_ORIGINS` to include your frontend domain
3. Set `COOKIE_DOMAIN` to your production domain
4. Ensure HTTPS is enabled (cookies will be marked secure)

### Next Steps

The documentation framework is now in place. When you add new endpoints:

1. Use proper Pydantic schemas for request/response models
2. Add comprehensive descriptions and examples
3. Include error response documentation
4. Tag endpoints appropriately for organization
5. Add security requirements for protected routes

The Swagger documentation will automatically update as you add new endpoints and models.
