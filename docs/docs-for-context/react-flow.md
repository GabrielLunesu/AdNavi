### Install React Flow with Vite (bun)

Source: https://reactflow.dev/learn

Installs a new React project using Vite with the React template and adds React Flow as a dependency using bun.

```bash
bunx create-vite my-react-flow-app --template react
cd my-react-flow-app
bun add @xyflow/react
bun run dev
```

--------------------------------

### Install React Flow with Vite (yarn)

Source: https://reactflow.dev/learn

Installs a new React project using Vite with the React template and adds React Flow as a dependency using yarn.

```bash
yarn create vite my-react-flow-app --template react
cd my-react-flow-app
yarn add @xyflow/react
yarn dev
```

--------------------------------

### Install React Flow with Vite (npm)

Source: https://reactflow.dev/learn

Installs a new React project using Vite with the React template and adds React Flow as a dependency using npm.

```bash
npm init vite my-react-flow-app -- --template react
cd my-react-flow-app
npm install @xyflow/react
npm run dev
```

--------------------------------

### Install React Flow with Vite (pnpm)

Source: https://reactflow.dev/learn

Installs a new React project using Vite with the React template and adds React Flow as a dependency using pnpm.

```bash
pnpm create vite my-react-flow-app --template react
cd my-react-flow-app
pnpm add @xyflow/react
pnpm run dev
```

--------------------------------

### React Flow Default Styles Setup (React)

Source: https://reactflow.dev/learn/customization/theming

Demonstrates how to set up a basic React Flow component with default nodes and edges. It imports necessary components and CSS, defines initial node and edge structures, and uses state management hooks for interactivity. This snippet serves as a starting point for building React Flow applications.

```tsx
import React, { useCallback } from 'react';
import {
  ReactFlow,
  Background,
  Controls,
  MiniMap,
  useNodesState,
  useEdgesState,
  addEdge,
  Position,
} from '@xyflow/react';

import '@xyflow/react/dist/style.css';


const nodeDefaults = {
  sourcePosition: Position.Right,
  targetPosition: Position.Left,
};

const initialNodes = [
  {
    id: '1',
    position: { x: 0, y: 150 },
    data: { label: 'default style 1' },
    ...nodeDefaults,
  },
  {
    id: '2',
    position: { x: 250, y: 0 },
    data: { label: 'default style 2' },
    ...nodeDefaults,
  },
  {
    id: '3',
    position: { x: 250, y: 150 },
    data: { label: 'default style 3' },
    ...nodeDefaults,
  },
  {
    id: '4',
    position: { x: 250, y: 300 },
    data: { label: 'default style 4' },
    ...nodeDefaults,
  },
];

const initialEdges = [
  {
    id: 'e1-2',
    source: '1',
    target: '2',
    animated: true,
  },
  {
    id: 'e1-3',
    source: '1',
    target: '3',
  },
  {
    id: 'e1-4',
    source: '1',
    target: '4',
  },
];

const Flow = () => {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect = useCallback(
    (params) => setEdges((els) => addEdge(params, els)),
    [],
  );

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      onConnect={onConnect}
      fitView
    >
      <Background />
      <Controls />
      <MiniMap />
    </ReactFlow>
  );
};

export default Flow;

```

--------------------------------

### React Flow Edge Toolbar Example Setup

Source: https://reactflow.dev/examples/edges/edge-toolbar

Sets up a React Flow instance with custom edge types for displaying a button and a toolbar on edges. It defines initial nodes and edges, and configures the ReactFlow component with custom edge types.

```typescript
import {
  Background,
  BackgroundVariant,
  Controls,
  Edge,
  EdgeTypes,
  MiniMap,
  Node,
  Position,
  ReactFlow,
} from '@xyflow/react';

import '@xyflow/react/dist/style.css';

import { EdgeWithToolbar } from './EdgeWithToolbar';
import { EdgeWithButton } from './EdgeWithButton';

const edgeTypes: EdgeTypes = {
  edgeButton: EdgeWithButton,
  edgeToolbar: EdgeWithToolbar,
};

const initialNodes: Node[] = [
  {
    id: '1',
    data: { label: 'Node 1' },
    position: { x: 150, y: 100 },
    sourcePosition: Position.Right,
    targetPosition: Position.Left,
  },
  {
    id: '2',
    data: { label: 'Node 2' },
    position: { x: 550, y: 0 },
    sourcePosition: Position.Right,
    targetPosition: Position.Left,
  },

  {
    id: '3',
    data: { label: 'Node 3' },
    position: { x: 0, y: 300 },
    sourcePosition: Position.Right,
    targetPosition: Position.Left,
  },
  {
    id: '4',
    data: { label: 'Node 4' },
    position: { x: 750, y: 200 },
    sourcePosition: Position.Right,
    targetPosition: Position.Left,
  },
];

const initialEdges: Edge[] = [
  {
    id: 'e1-2',
    source: '1',
    target: '2',
    type: 'edgeButton',
  },

  {
    id: 'e3-4',
    source: '3',
    target: '4',
    type: 'edgeToolbar',
  },
];

export default function EdgeToolbarExample() {
  return (
    <ReactFlow
      defaultNodes={initialNodes}
      defaultEdges={initialEdges}
      fitView
      edgeTypes={edgeTypes}
    >
      <Background />
      <MiniMap />
      <Controls />
    </ReactFlow>
  );
}

```

--------------------------------

### Basic React Flow Setup with ReactFlowProvider

Source: https://reactflow.dev/learn/advanced-use/hooks-providers

This example demonstrates a basic setup of React Flow using the ReactFlowProvider. It initializes nodes, edges, and provides controls and background. The ReactFlowProvider is essential for enabling hooks and managing flow state outside the main ReactFlow component.

```jsx
import React, { useCallback } from 'react';
import {
  Background,
  ReactFlow,
  ReactFlowProvider,
  useNodesState,
  useEdgesState,
  addEdge,
  Controls,
} from '@xyflow/react';

import Sidebar from './Sidebar';
import '@xyflow/react/dist/style.css';

const initialNodes = [
  {
    id: 'provider-1',
    type: 'input',
    data: { label: 'Node 1' },
    position: { x: 250, y: 5 },
  },
  { id: 'provider-2', data: { label: 'Node 2' }, position: { x: 100, y: 100 } },
  { id: 'provider-3', data: { label: 'Node 3' }, position: { x: 400, y: 100 } },
  { id: 'provider-4', data: { label: 'Node 4' }, position: { x: 400, y: 200 } },
];

const initialEdges = [
  {
    id: 'provider-e1-2',
    source: 'provider-1',
    target: 'provider-2',
    animated: true,
  },
  { id: 'provider-e1-3', source: 'provider-1', target: 'provider-3' },
];

const ProviderFlow = () => {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);
  const onConnect = useCallback(
    (params) => setEdges((els) => addEdge(params, els)),
    [],
  );

  return (
    <div className="providerflow">
      <ReactFlowProvider>
        <div className="reactflow-wrapper">
          <ReactFlow
            nodes={nodes}
            edges={edges}
            onNodesChange={onNodesChange}
            onEdgesChange={onEdgesChange}
            onConnect={onConnect}
            fitView
          >
            <Controls />
            <Background />
          </ReactFlow>
        </div>
        <Sidebar nodes={nodes} setNodes={setNodes} />
      </ReactFlowProvider>
    </div>
  );
};

export default ProviderFlow;

```

--------------------------------

### Install Placeholder Node with npm, yarn, pnpm, or bun

Source: https://reactflow.dev/ui/components/placeholder-node

Instructions for installing the Placeholder Node component using different package managers. This component requires a prior setup following the project's prerequisites.

```bash
npx shadcn@latest add https://ui.reactflow.dev/placeholder-node
```

```bash
pnpm dlx shadcn@latest add https://ui.reactflow.dev/placeholder-node
```

```bash
yarn dlx shadcn@latest add https://ui.reactflow.dev/placeholder-node
```

```bash
bun x shadcn@latest add https://ui.reactflow.dev/placeholder-node
```

--------------------------------

### React Flow App Setup with Resizable Nodes

Source: https://reactflow.dev/examples/nodes/node-resizer

Sets up the main React Flow component, defining node types, initial nodes and edges, and configuring background and controls. It imports and uses custom node components designed for resizing.

```jsx
import {
  ReactFlow,
  Background,
  BackgroundVariant,
  Controls,
} from '@xyflow/react';

import ResizableNode from './ResizableNode';
import ResizableNodeSelected from './ResizableNodeSelected';
import CustomResizerNode from './CustomResizerNode';

import '@xyflow/react/dist/style.css';

const nodeTypes = {
  ResizableNode,
  ResizableNodeSelected,
  CustomResizerNode,
};

const initialNodes = [
  {
    id: '1',
    type: 'ResizableNode',
    data: { label: 'NodeResizer' },
    position: { x: 0, y: 50 },
  },
  {
    id: '2',
    type: 'ResizableNodeSelected',
    data: { label: 'NodeResizer when selected' },
    position: { x: -100, y: 150 },
  },
  {
    id: '3',
    type: 'CustomResizerNode',
    data: { label: 'Custom Resize Icon' },
    position: { x: 150, y: 150 },
    style: {
      height: 100,
    },
  },
];

const initialEdges = [];

export default function NodeToolbarExample() {
  return (
    <ReactFlow
      defaultNodes={initialNodes}
      defaultEdges={initialEdges}
      minZoom={0.2}
      maxZoom={4}
      fitView
      nodeTypes={nodeTypes}
      fitViewOptions={{ padding: 0.5 }}>
      <Background variant={BackgroundVariant.Dots} />
      <Controls />
    </ReactFlow>
  );
}
```

--------------------------------

### React Flow Easy Connect Setup (JavaScript)

Source: https://reactflow.dev/examples/nodes/easy-connect

Sets up a React Flow component with custom nodes and edges for easy connection. It utilizes hooks like `useNodesState` and `useEdgesState` to manage node and edge states, and `addEdge` for connection logic. Custom components for nodes, edges, and connection lines are defined.

```javascript
import React, { useCallback } from 'react';

import {
  Background,
  ReactFlow,
  addEdge,
  useNodesState,
  useEdgesState,
  MarkerType,
} from '@xyflow/react';

import '@xyflow/react/dist/style.css';

import CustomNode from './CustomNode';
import FloatingEdge from './FloatingEdge';
import CustomConnectionLine from './CustomConnectionLine';

const initialNodes = [
  {
    id: '1',
    type: 'custom',
    position: { x: 0, y: 0 },
  },
  {
    id: '2',
    type: 'custom',
    position: { x: 250, y: 320 },
  },
  {
    id: '3',
    type: 'custom',
    position: { x: 40, y: 300 },
  },
  {
    id: '4',
    type: 'custom',
    position: { x: 300, y: 0 },
  },
];

const initialEdges = [];

const connectionLineStyle = {
  stroke: '#b1b1b7',
};

const nodeTypes = {
  custom: CustomNode,
};

const edgeTypes = {
  floating: FloatingEdge,
};

const defaultEdgeOptions = {
  type: 'floating',
  markerEnd: {
    type: MarkerType.ArrowClosed,
    color: '#b1b1b7',
  },
};

const EasyConnectExample = () => {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect = useCallback(
    (params) => setEdges((eds) => addEdge(params, eds)),
    [setEdges],
  );

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      onConnect={onConnect}
      fitView
      nodeTypes={nodeTypes}
      edgeTypes={edgeTypes}
      defaultEdgeOptions={defaultEdgeOptions}
      connectionLineComponent={CustomConnectionLine}
      connectionLineStyle={connectionLineStyle}
    >
      <Background />
    </ReactFlow>
  );
};

export default EasyConnectExample;

```

--------------------------------

### Install Zoom Slider Component using npm, pnpm, yarn, or bun

Source: https://reactflow.dev/ui/components/zoom-slider

This section provides commands for installing the Zoom Slider component using various package managers. It requires prior setup following the component's prerequisites.

```bash
npx shadcn@latest add https://ui.reactflow.dev/zoom-slider
```

```bash
pnpm dlx shadcn@latest add https://ui.reactflow.dev/zoom-slider
```

```bash
yarn dlx shadcn@latest add https://ui.reactflow.dev/zoom-slider
```

```bash
bun x shadcn@latest add https://ui.reactflow.dev/zoom-slider
```

--------------------------------

### React Flow: Feature Overview Example

Source: https://reactflow.dev/examples

This example provides an overview of React Flow's basic features, including built-in node and edge types, sub-flows, and components like NodeToolbar and NodeResizer. It serves as a starting point for understanding core functionalities.

```javascript
import React from 'react';
import ReactFlow from 'reactflow';

import 'reactflow/dist/base.css';

const nodes = [
  {
    id: '1',
    type: 'input',
    data: { label: 'Node 1' },
    position: { x: 250, y: 5 },
  },
  // ... other nodes
];

const edges = [
  { id: 'e1-2', source: '1', target: '2', label: 'edge label 1' },
  // ... other edges
];

function Flow() {
  return <ReactFlow nodes={nodes} edges={edges} onConnect={onConnect} fitView />;
}

export default Flow;
```

--------------------------------

### Install React Flow (New API)

Source: https://reactflow.dev/learn/troubleshooting/migrate-to-v11

Illustrates the new npm installation command for 'reactflow' from the '@xyflow/react' scope. This is the current recommended way to install React Flow.

```bash
npm install reactflow
```

--------------------------------

### React Flow: Easy Connect Example

Source: https://reactflow.dev/examples

This example transforms the entire node into a draggable handle, allowing connections to be initiated from any part of the node. It simplifies the connection process for users.

```javascript
import React, { useState, useCallback } from 'react';
import ReactFlow, { addEdge, applyNodeChanges, applyEdgeChanges } from 'reactflow';

import 'reactflow/dist/base.css';

const initialNodes = [
  {
    id: '1',
    data: { label: 'Source Node' },
    position: { x: 100, y: 100 },
  },
  {
    id: '2',
    data: { label: 'Target Node' },
    position: { x: 400, y: 100 },
  },
];

const initialEdges = [];

function EasyConnectFlow() {
  const [nodes, setNodes] = useState(initialNodes);
  const [edges, setEdges] = useState(initialEdges);

  const onConnect = useCallback(
    (params) => setEdges((eds) => addEdge(params, eds)),
    [setEdges]
  );

  return (
    <div style={{ height: '100%' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onConnect={onConnect}
        fitView
        // The node component itself would need to be configured to act as a handle
      />
    </div>
  );
}

export default EasyConnectFlow;
```

--------------------------------

### React Flow Setup for Image Download

Source: https://reactflow.dev/examples/misc/download-image

This React component sets up the React Flow interface, including nodes, edges, controls, and background. It imports necessary components from '@xyflow/react' and custom elements like 'DownloadButton' and 'CustomNode'. The 'html-to-image' library is implicitly used by the 'DownloadButton' component for the image export functionality.

```jsx
import React, { useCallback } from 'react';
import {
  ReactFlow,
  useNodesState,
  useEdgesState,
  addEdge,
  Controls,
  Background,
} from '@xyflow/react';

import '@xyflow/react/dist/style.css';

import DownloadButton from './DownloadButton';
import CustomNode from './CustomNode';
import { initialNodes, initialEdges } from './initialElements';

const connectionLineStyle = { stroke: '#ffff' };
const snapGrid = [25, 25];
const nodeTypes = {
  custom: CustomNode,
};

const defaultEdgeOptions = {
  animated: true,
  type: 'smoothstep',
};

const defaultViewport = { x: 0, y: 0, zoom: 1.5 };

const DownloadImageFlow = () => {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect = useCallback(
    (params) => setEdges((eds) => addEdge(params, eds)),
    [],
  );

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      onConnect={onConnect}
      nodeTypes={nodeTypes}
      connectionLineStyle={connectionLineStyle}
      connectionLineType="smoothstep"
      snapToGrid={true}
      snapGrid={snapGrid}
      defaultViewport={defaultViewport}
      fitView
      attributionPosition="bottom-left"
      defaultEdgeOptions={defaultEdgeOptions}
      className="download-image"
    >
      <Controls />
      <Background />
      <DownloadButton />
    </ReactFlow>
  );
};

export default DownloadImageFlow;
```

--------------------------------

### Install Node Appendix with npm, pnpm, yarn, or bun

Source: https://reactflow.dev/ui/components/node-appendix

These commands demonstrate how to install the Node Appendix component using different package managers. Ensure you have the necessary prerequisites installed before running these commands.

```bash
npx shadcn@latest add https://ui.reactflow.dev/node-appendix
```

```bash
pnpm dlx shadcn@latest add https://ui.reactflow.dev/node-appendix
```

```bash
yarn dlx shadcn@latest add https://ui.reactflow.dev/node-appendix
```

```bash
bun x shadcn@latest add https://ui.reactflow.dev/node-appendix
```

--------------------------------

### React Flow App Setup with Custom Nodes

Source: https://reactflow.dev/examples/interaction/computing-flows

Initializes a React Flow component with custom node types (text, result, uppercase). It sets up the initial nodes and edges, and defines the logic for connecting them using `useNodesState`, `useEdgesState`, and `addEdge`. Dependencies include React, React Flow, and custom node components.

```typescript
import {
  useCallback
} from 'react';
import {
  ReactFlow,
  Controls,
  addEdge,
  useNodesState,
  useEdgesState,
  Background,
  type Edge,
  type OnConnect,
} from '@xyflow/react';

import '@xyflow/react/dist/style.css';

import TextNode from './TextNode';
import ResultNode from './ResultNode';
import UppercaseNode from './UppercaseNode';
import { type MyNode } from './initialElements';

const nodeTypes = {
  text: TextNode,
  result: ResultNode,
  uppercase: UppercaseNode,
};

const initNodes: MyNode[] = [
  {
    id: '1',
    type: 'text',
    data: {
      text: 'hello',
    },
    position: { x: -100, y: -50 },
  },
  {
    id: '2',
    type: 'text',
    data: {
      text: 'world',
    },
    position: { x: 0, y: 100 },
  },
  {
    id: '3',
    type: 'uppercase',
    data: { text: '' },
    position: { x: 100, y: -100 },
  },
  {
    id: '4',
    type: 'result',
    data: {},
    position: { x: 300, y: -75 },
  },
];

const initEdges: Edge[] = [
  {
    id: 'e1-3',
    source: '1',
    target: '3',
  },
  {
    id: 'e3-4',
    source: '3',
    target: '4',
  },
  {
    id: 'e2-4',
    source: '2',
    target: '4',
  },
];

const CustomNodeFlow = () => {
  const [nodes, , onNodesChange] = useNodesState(initNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initEdges);

  const onConnect: OnConnect = useCallback(
    (connection) => setEdges((eds) => addEdge(connection, eds)),
    [setEdges],
  );

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      onConnect={onConnect}
      nodeTypes={nodeTypes}
      fitView
    >
      <Controls />
      <Background />
    </ReactFlow>
  );
};

export default CustomNodeFlow;

```

--------------------------------

### React Flow Example with Resizable Nodes

Source: https://reactflow.dev/api-reference/components/node-resizer

This example showcases a React Flow setup that utilizes different types of resizable nodes, including a standard resizable node, one that appears when selected, and a node with custom resize controls. It configures the ReactFlow component with these custom node types and initial data.

```javascript
import {
  ReactFlow,
  Background,
  BackgroundVariant,
  Controls,
} from '@xyflow/react';
 
import ResizableNode from './ResizableNode';
import ResizableNodeSelected from './ResizableNodeSelected';
import CustomResizerNode from './CustomResizerNode';
 
import '@xyflow/react/dist/style.css';
 
const nodeTypes = {
  ResizableNode,
  ResizableNodeSelected,
  CustomResizerNode,
};
 
const initialNodes = [
  {
    id: '1',
    type: 'ResizableNode',
    data: { label: 'NodeResizer' },
    position: { x: 0, y: 50 },
  },
  {
    id: '2',
    type: 'ResizableNodeSelected',
    data: { label: 'NodeResizer when selected' },
    position: { x: -100, y: 150 },
  },
  {
    id: '3',
    type: 'CustomResizerNode',
    data: { label: 'Custom Resize Icon' },
    position: { x: 150, y: 150 },
    style: {
      height: 100,
    },
  },
];
 
const initialEdges = [];
 
export default function NodeToolbarExample() {
  return (
    <ReactFlow
      defaultNodes={initialNodes}
      defaultEdges={initialEdges}
      minZoom={0.2}
      maxZoom={4}
      fitView
      nodeTypes={nodeTypes}
      fitViewOptions={{ padding: 0.5 }}
    >
      <Background variant={BackgroundVariant.Dots} />
      <Controls />
    </ReactFlow>
  );
}
```

--------------------------------

### Install Base Handle Component using npm, pnpm, yarn, or bun

Source: https://reactflow.dev/ui/components/base-handle

Commands to install the Base Handle component using various package managers. Ensure prerequisites are met before installation.

```bash
npx shadcn@latest add https://ui.reactflow.dev/base-handle
```

```bash
pnpm dlx shadcn@latest add https://ui.reactflow.dev/base-handle
```

```bash
yarn dlx shadcn@latest add https://ui.reactflow.dev/base-handle
```

```bash
bun x shadcn@latest add https://ui.reactflow.dev/base-handle
```

--------------------------------

### Install Node Tooltip with bun

Source: https://reactflow.dev/ui/components/node-tooltip

Installs the Node Tooltip component using bun via the shadcn CLI. Ensure you have the necessary prerequisites installed before running this command.

```bash
bun x shadcn@latest add https://ui.reactflow.dev/node-tooltip
```

--------------------------------

### Install React Flow Package

Source: https://reactflow.dev/learn/concepts/building-a-flow

Installs the necessary React Flow package using different package managers like npm, pnpm, yarn, and bun. Ensure you have Node.js and a package manager installed.

```bash
npm install @xyflow/react
```

```bash
pnpm add @xyflow/react
```

```bash
yarn add @xyflow/react
```

```bash
bun add @xyflow/react
```

--------------------------------

### React Flow: Node Position Animation Example

Source: https://reactflow.dev/examples

An example demonstrating smooth transitions between different graph layouts with interactive controls. This enhances the user experience by animating node movements.

```javascript
import React, { useState, useCallback } from 'react';
import ReactFlow, { applyNodeChanges, Controls, Background } from 'reactflow';

import 'reactflow/dist/base.css';

const initialNodes = [
  { id: '1', data: { label: 'Node 1' }, position: { x: 100, y: 100 } },
  { id: '2', data: { label: 'Node 2' }, position: { x: 300, y: 100 } },
];

function AnimatedLayoutFlow() {
  const [nodes, setNodes] = useState(initialNodes);

  const onNodesChange = useCallback(
    (changes) => {
      setNodes((nds) => applyNodeChanges(changes, nds));
    },
    [setNodes]
  );

  const animateLayout = () => {
    // Logic to calculate new positions for nodes to animate layout change
    setNodes(currentNodes => {
      const newNodes = currentNodes.map(node => {
        // Example: shift nodes to the right
        return { ...node, position: { x: node.position.x + 50, y: node.position.y } };
      });
      return newNodes;
    });
  };

  return (
    <div style={{ height: '100%' }}>
      <ReactFlow
        nodes={nodes}
        onNodesChange={onNodesChange}
        fitView
        nodesDraggable={false} // Example: disable dragging to focus on layout animation
      >
        <button onClick={animateLayout} style={{ position: 'absolute', top: 10, left: 10, zIndex: 10 }}>
          Animate Layout
        </button>
        <Background />
        <Controls />
      </ReactFlow>
    </div>
  );
}

export default AnimatedLayoutFlow;
```

--------------------------------

### React Flow App Setup with Rotatable Node

Source: https://reactflow.dev/examples/nodes/rotatable-node

Sets up the main React Flow component, registering the custom 'rotatableNode' type and providing initial elements. It requires the '@xyflow/react' package and the associated CSS styles.

```jsx
import React from 'react';
import { ReactFlow, Background } from '@xyflow/react';
import '@xyflow/react/dist/style.css';

import RotatableNode from './RotatableNode';
import { nodes, edges } from './initialElements';

const nodeTypes = {
  rotatableNode: RotatableNode,
};

function Flow() {
  return (
    <ReactFlow
      nodeTypes={nodeTypes}
      defaultNodes={nodes}
      defaultEdges={edges}
      fitView
    >
      <Background />
    </ReactFlow>
  );
}

export default Flow;
```

--------------------------------

### Install Node Tooltip with npm

Source: https://reactflow.dev/ui/components/node-tooltip

Installs the Node Tooltip component using npm via the shadcn CLI. Ensure you have the necessary prerequisites installed before running this command.

```bash
npx shadcn@latest add https://ui.reactflow.dev/node-tooltip
```

--------------------------------

### React Flow Base Styling with JavaScript

Source: https://reactflow.dev/examples/styling/base-style

This React component demonstrates how to apply the mandatory base style for React Flow. It initializes nodes and edges and renders a basic flow with background, controls, and a minimap. Ensure you have '@xyflow/react' installed as a dependency.

```jsx
import React, { useCallback } from 'react';
import {
  ReactFlow,
  Background,
  Controls,
  MiniMap,
  useNodesState,
  useEdgesState,
  addEdge,
  Position,
} from '@xyflow/react';

import '@xyflow/react/dist/base.css';

const nodeDefaults = {
  sourcePosition: Position.Right,
  targetPosition: Position.Left,
};

const initialNodes = [
  {
    id: '1',
    position: { x: 0, y: 150 },
    data: { label: 'base style 1' },
    ...nodeDefaults,
  },
  {
    id: '2',
    position: { x: 250, y: 0 },
    data: { label: 'base style 2' },
    ...nodeDefaults,
  },
  {
    id: '3',
    position: { x: 250, y: 150 },
    data: { label: 'base style 3' },
    ...nodeDefaults,
  },
  {
    id: '4',
    position: { x: 250, y: 300 },
    data: { label: 'base style 4' },
    ...nodeDefaults,
  },
];

const initialEdges = [
  {
    id: 'e1-2',
    source: '1',
    target: '2',
  },
  {
    id: 'e1-3',
    source: '1',
    target: '3',
  },
  {
    id: 'e1-4',
    source: '1',
    target: '4',
  },
];

const Flow = () => {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect = useCallback(
    (params) => setEdges((els) => addEdge(params, els)),
    [],
  );

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      onConnect={onConnect}
      fitView
    >
      <Background />
      <Controls />
      <MiniMap />
    </ReactFlow>
  );
};

export default Flow;

```

--------------------------------

### Install React Flow Renderer (Old API)

Source: https://reactflow.dev/learn/troubleshooting/migrate-to-v11

Demonstrates the old npm installation command for 'react-flow-renderer'. This package has been renamed in newer versions.

```bash
npm install react-flow-renderer
```

--------------------------------

### React Flow Setup with Contextual Zoom Nodes

Source: https://reactflow.dev/examples/interaction/contextual-zoom

This snippet sets up a React Flow graph with custom nodes that can dynamically change their content based on the zoom level. It initializes nodes, edges, defines custom node types, and configures React Flow with features like background, minimap, and controls. The `defaultViewport` sets an initial zoom level.

```jsx
import React, { useCallback } from 'react';
import {
  Background,
  ReactFlow,
  useNodesState,
  useEdgesState,
  addEdge,
  MiniMap,
  Controls,
} from '@xyflow/react';

import '@xyflow/react/dist/style.css';

import ZoomNode from './ZoomNode';

const snapGrid = [20, 20];
const nodeTypes = {
  zoom: ZoomNode,
};

const initialNodes = [
  {
    id: '1',
    type: 'zoom',
    data: {
      content: <>Zoom to toggle content and placeholder</>,
    },
    position: { x: 0, y: 0 },
  },
  {
    id: '2',
    type: 'zoom',
    data: { content: <>this is a node with some lines of text in it.</> },
    position: { x: 200, y: 0 },
  },
  {
    id: '3',
    type: 'zoom',
    data: { content: <>this is another node with some more text.</> },
    position: { x: 400, y: 0 },
  },
];

const initialEdges = [
  {
    id: 'e1-2',
    source: '1',
    target: '2',
    animated: true,
  },
  {
    id: 'e2-3',
    source: '2',
    target: '3',
    animated: true,
  },
];

const defaultViewport = { x: 0, y: 0, zoom: 1.5 };

const ContextualZoomFlow = () => {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);
  const onConnect = useCallback(
    (params) => setEdges((eds) => addEdge({ ...params, animated: true },eds)),
    [],
  );

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      onConnect={onConnect}
      nodeTypes={nodeTypes}
      snapToGrid={true}
      snapGrid={snapGrid}
      defaultViewport={defaultViewport}
      attributionPosition="top-right"
      fitView
    >
      <Background />
      <MiniMap />
      <Controls />
    </ReactFlow>
  );
};

export default ContextualZoomFlow;

```

--------------------------------

### Basic React Flow Component Implementation

Source: https://reactflow.dev/learn/getting-started/installation-and-requirements

A React component that sets up and renders the React Flow graph. It includes initializing nodes and edges, defining handlers for node/edge changes and connections, and applying necessary CSS.

```jsx
import { useState, useCallback } from 'react';
import { ReactFlow, applyNodeChanges, applyEdgeChanges, addEdge } from '@xyflow/react';
import '@xyflow/react/dist/style.css';

const initialNodes = [
  { id: 'n1', position: { x: 0, y: 0 }, data: { label: 'Node 1' } },
  { id: 'n2', position: { x: 0, y: 100 }, data: { label: 'Node 2' } },
];
const initialEdges = [{ id: 'n1-n2', source: 'n1', target: 'n2' }];

export default function App() {
  const [nodes, setNodes] = useState(initialNodes);
  const [edges, setEdges] = useState(initialEdges);

  const onNodesChange = useCallback(
    (changes) => setNodes((nodesSnapshot) => applyNodeChanges(changes, nodesSnapshot)),
    [],
  );
  const onEdgesChange = useCallback(
    (changes) => setEdges((edgesSnapshot) => applyEdgeChanges(changes, edgesSnapshot)),
    [],
  );
  const onConnect = useCallback(
    (params) => setEdges((edgesSnapshot) => addEdge(params, edgesSnapshot)),
    [],
  );

  return (
    <div style={{ width: '100vw', height: '100vh' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        fitView
      />
    </div>
  );
}
```

--------------------------------

### Install Button Edge Component with npm, pnpm, yarn, bun

Source: https://reactflow.dev/ui/components/button-edge

Commands to install the Button Edge component using various package managers. Ensure prerequisites are met before installation.

```bash
npx shadcn@latest add https://ui.reactflow.dev/button-edge
```

```bash
pnpm dlx shadcn@latest add https://ui.reactflow.dev/button-edge
```

```bash
yarn dlx shadcn@latest add https://ui.reactflow.dev/button-edge
```

```bash
bun x shadcn@latest add https://ui.reactflow.dev/button-edge
```

--------------------------------

### Initialize React Project with Vite

Source: https://reactflow.dev/learn/getting-started/installation-and-requirements

Commands to create a new React project using Vite across different package managers (npm, pnpm, yarn, bun). Vite is a fast build tool that significantly improves the frontend development experience.

```bash
npm init vite my-react-flow-app -- --template react
```

```bash
pnpm create vite my-react-flow-app --template react
```

```bash
yarn create vite my-react-flow-app --template react
```

```bash
bunx create-vite my-react-flow-app --template react
```

--------------------------------

### Install Node Search with bun

Source: https://reactflow.dev/ui/components/node-search

Installs the Node Search component using bun and shadcn/ui. Bun is a fast JavaScript runtime and toolkit.

```bash
bun x shadcn@latest add https://ui.reactflow.dev/node-search
```

--------------------------------

### React Flow Drag Handle Node Configuration

Source: https://reactflow.dev/examples/nodes/drag-handle

This snippet shows the main React Flow component setup. It defines custom node types, initial nodes with a specified `dragHandle` class, and the necessary state management for nodes and edges. It renders a React Flow instance with a background and applies the custom node type.

```jsx
import React from 'react';
import {
  ReactFlow,
  useNodesState,
  useEdgesState,
  Background,
} from '@xyflow/react';

import DragHandleNode from './DragHandleNode';
import '@xyflow/react/dist/style.css';

const nodeTypes = {
  dragHandleNode: DragHandleNode,
};

const initialNodes = [
  {
    id: '2',
    type: 'dragHandleNode',

    // Specify the custom class acting as a drag handle
    dragHandle: '.drag-handle__custom',
    position: { x: 200, y: 200 },
  },
];

const DragHandleFlow = () => {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      nodeTypes={nodeTypes}
      fitView
    >
      <Background />
    </ReactFlow>
  );
};

export default DragHandleFlow;
```

--------------------------------

### Install Node Tooltip with pnpm

Source: https://reactflow.dev/ui/components/node-tooltip

Installs the Node Tooltip component using pnpm via the shadcn CLI. Ensure you have the necessary prerequisites installed before running this command.

```bash
pnpm dlx shadcn@latest add https://ui.reactflow.dev/node-tooltip
```

--------------------------------

### Install Node Tooltip with yarn

Source: https://reactflow.dev/ui/components/node-tooltip

Installs the Node Tooltip component using yarn via the shadcn CLI. Ensure you have the necessary prerequisites installed before running this command.

```bash
yarn dlx shadcn@latest add https://ui.reactflow.dev/node-tooltip
```

--------------------------------

### Install DevTools with npm, pnpm, yarn, or bun

Source: https://reactflow.dev/ui/components/devtools

These commands demonstrate how to add the React Flow DevTools to your project using various package managers. This installation method relies on shadcn/ui for component management and requires specific prerequisites.

```bash
npx shadcn@latest add https://ui.reactflow.dev/devtools
```

```bash
pnpm dlx shadcn@latest add https://ui.reactflow.dev/devtools
```

```bash
yarn dlx shadcn@latest add https://ui.reactflow.dev/devtools
```

```bash
bun x shadcn@latest add https://ui.reactflow.dev/devtools
```

--------------------------------

### React Flow Drag and Drop with Pointer Events

Source: https://reactflow.dev/examples/interaction/drag-and-drop

Implements drag and drop functionality in React Flow using the Pointer Events API. This approach ensures consistent behavior across mouse and touch devices. It requires the '@xyflow/react' library and basic React setup.

```tsx
import {
  useCallback
} from 'react';
import {
  Background,
  Connection,
  Controls,
  ReactFlow,
  ReactFlowProvider,
  addEdge,
  useEdgesState,
  useNodesState,
} from '@xyflow/react';

import '@xyflow/react/dist/style.css';

import { Sidebar } from './Sidebar';
import { DnDProvider } from './useDnD';

const initialNodes = [
  {
    id: '1',
    type: 'input',
    data: { label: 'input node' },
    position: { x: 250, y: 5 },
  },
];

function DnDFlow() {
  const [nodes, _, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);

  const onConnect = useCallback(
    (params: Connection) => setEdges((eds) => addEdge(params, eds)),
    [],
  );

  return (
    <div className="dndflow">
      <div className="reactflow-wrapper">
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          onConnect={onConnect}
          fitView
        >
          <Controls />
          <Background />
        </ReactFlow>
      </div>
      <Sidebar />
    </div>
  );
}

export default () => (
  <ReactFlowProvider>
    <DnDProvider>
      <DnDFlow />
    </DnDProvider>
  </ReactFlowProvider>
);

```

--------------------------------

### Install Node Search with npm

Source: https://reactflow.dev/ui/components/node-search

Installs the Node Search component using npm and shadcn/ui. Ensure you have the necessary prerequisites before running this command.

```bash
npx shadcn@latest add https://ui.reactflow.dev/node-search
```

--------------------------------

### React Flow: Node Toolbar Example

Source: https://reactflow.dev/examples

Displays a context-sensitive toolbar with buttons adjacent to a selected node. This allows for quick access to actions related to that specific node.

```javascript
import React, { useState, useCallback } from 'react';
import ReactFlow, { addEdge, applyNodeChanges, applyEdgeChanges, NodeToolbar, useReactFlow } from 'reactflow';

import 'reactflow/dist/base.css';

const initialNodes = [
  { id: '1', data: { label: 'Node with Toolbar' }, position: { x: 100, y: 100 } },
];

function NodeToolbarFlow() {
  const [nodes, setNodes] = useState(initialNodes);
  const { getNode } = useReactFlow();

  const onNodesChange = useCallback(
    (changes) => setNodes((nds) => applyNodeChanges(changes, nds)),
    [setNodes]
  );

  const handleNodeClick = useCallback((event, node) => {
    console.log('Node clicked:', node.id);
    // Logic to show toolbar or perform action
  }, []);

  return (
    <div style={{ height: '100%' }}>
      <ReactFlow
        nodes={nodes}
        onNodesChange={onNodesChange}
        onNodeClick={handleNodeClick}
        fitView
      >
        {/* Render NodeToolbar conditionally based on node selection */}
        {nodes.map(node => (
          <NodeToolbar key={node.id} isVisible={node.selected} position={node.position} offset={20}>
            {/* Toolbar buttons here */}
            <button>Action 1</button>
            <button>Action 2</button>
          </NodeToolbar>
        ))}
        <Controls />
      </ReactFlow>
    </div>
  );
}

export default NodeToolbarFlow;
```

--------------------------------

### Basic React Flow Setup with TypeScript

Source: https://reactflow.dev/learn/advanced-use/typescript

Demonstrates the fundamental setup of React Flow using TypeScript. It initializes nodes and edges, defines event handlers for node and edge changes, and connection logic. Includes common types like Node, Edge, FitViewOptions, and OnConnect.

```typescript
import {
  useState,
  useCallback
} from 'react';
import {
  ReactFlow,
  addEdge,
  applyNodeChanges,
  applyEdgeChanges,
  type Node,
  type Edge,
  type FitViewOptions,
  type OnConnect,
  type OnNodesChange,
  type OnEdgesChange,
  type OnNodeDrag,
  type DefaultEdgeOptions,
} from '@xyflow/react';

const initialNodes: Node[] = [
  { id: '1', data: { label: 'Node 1' }, position: { x: 5, y: 5 } },
  { id: '2', data: { label: 'Node 2' }, position: { x: 5, y: 100 } },
];

const initialEdges: Edge[] = [{ id: 'e1-2', source: '1', target: '2' }];

const fitViewOptions: FitViewOptions = {
  padding: 0.2,
};

const defaultEdgeOptions: DefaultEdgeOptions = {
  animated: true,
};

const onNodeDrag: OnNodeDrag = (_, node) => {
  console.log('drag event', node.data);
};

function Flow() {
  const [nodes, setNodes] = useState<Node[]>(initialNodes);
  const [edges, setEdges] = useState<Edge[]>(initialEdges);

  const onNodesChange: OnNodesChange = useCallback(
    (changes) => setNodes((nds) => applyNodeChanges(changes, nds)),
    [setNodes],
  );
  const onEdgesChange: OnEdgesChange = useCallback(
    (changes) => setEdges((eds) => applyEdgeChanges(changes, eds)),
    [setEdges],
  );
  const onConnect: OnConnect = useCallback(
    (connection) => setEdges((eds) => addEdge(connection, eds)),
    [setEdges],
  );

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      onConnect={onConnect}
      onNodeDrag={onNodeDrag}
      fitView
      fitViewOptions={fitViewOptions}
      defaultEdgeOptions={defaultEdgeOptions}
    />
  );
}

```

--------------------------------

### Install Button Handle with bun

Source: https://reactflow.dev/ui/components/button-handle

Installs the Button Handle component using bun. This command adds the necessary package to your project's dependencies.

```bash
bun x shadcn@latest add https://ui.reactflow.dev/button-handle
```