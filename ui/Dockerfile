# Build stage
FROM node:20-alpine AS build
WORKDIR /app

# Accept build arguments for Next.js public env vars
ARG NEXT_PUBLIC_API_BASE
ENV NEXT_PUBLIC_API_BASE=${NEXT_PUBLIC_API_BASE}

# Install dependencies first (better caching)
COPY package.json package-lock.json* ./
RUN npm ci --no-audit --no-fund

# Copy source
COPY . .

# Build Next.js app
ENV NODE_ENV=production
RUN npm run build

# Runtime stage
FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
# INSTALL CURL
RUN apk add --no-cache curl

# Create non-root user
RUN addgroup -S nodejs && adduser -S nextjs -G nodejs

# Copy only what we need to run
COPY --from=build /app/package.json ./package.json
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/.next ./.next
COPY --from=build /app/public ./public

# Next.js default port
EXPOSE 3000

USER nextjs
CMD ["npm", "run", "start"]


