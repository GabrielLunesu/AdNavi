// Health check endpoint for Docker healthcheck
export async function GET() {
  return Response.json({ status: 'ok' }, { status: 200 });
}

