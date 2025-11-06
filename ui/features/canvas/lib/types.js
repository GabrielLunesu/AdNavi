// WHAT: JSDoc typedefs for Canvas shapes (JSX project)
// WHY: Provide editor hints and validate mapping contracts without TypeScript
// REFERENCES: docs/canvas/01-functional-spec.md

/**
 * @typedef {Object} CanvasNode
 * @property {string} id
 * @property {string} type - 'campaign' | 'adset' | 'ad'
 * @property {{x:number,y:number}} position
 * @property {Object} data - { name, status, platform, kpis }
 */

/**
 * @typedef {Object} CanvasEdge
 * @property {string} id
 * @property {string} source
 * @property {string} target
 * @property {boolean} [animated]
 */

export const __types = {};

