// WHAT: Central export for all API clients and adapters.
// WHY: Simplifies imports in UI components and provides a single point
//      of reference for backend interactions.

import * as campaignsApiClient from './campaignsApiClient';
import * as campaignsAdapter from './campaignsAdapter';

export { campaignsApiClient, campaignsAdapter };

