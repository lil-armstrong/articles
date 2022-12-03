# How to setup path aliases in Vite 2 & Typescript

> Have you ever thought of how to get rid of imports that look like ``../../assets/*`` or ``../../../assets/*``.

#### Reasons you need this
1. You need something fancy and very easy to reference.
2. Another reason you would need this is in a scenario where you created some files in a directory and suddenly moved those files to another directory, maybe nested within or outside but within the root of the project.

It can be very frustrating to try resolving the modules in each individual files. So you would want something that can easily allow you to refer to the root of the project and map the respective paths from that point.

In this tutorial, I will be using the alias ``@`` as a reference to the root of the project.
In order to follow this tutorial, you need to scaffold a react project using vite. Although I am using react to demonstrate this, you can do the same for other frintend frameworks like Vue and AngularJS as long as Typescript is supported.
> [Click here](https://vitejs.dev/guide/#scaffolding-your-first-vite-project) to learn how to scaffold a new vite app.
Follow the following steps to set a path alias for both typescript and Vite

## Steps to take
1. In your project directory, open ``tsconfig.json`` file and add the following entries to the ``compilerOptions`` key. Usually your project root has a src folder where all the source codes exist at. Set that as teh base url.
```js
{
	"compilerOptions": {
		...//other configs
		"baseUrl": "src",
		"paths":{
			"@/*": ["./*"]
		}
	}
}
```
For more information on tsconfig paths mapping & module resolution heuristics: [Click here](https://www.typescriptlang.org/docs/handbook/module-resolution.html#path-mapping)

The above configuration, informs typescript of to map module names, that matches the grob pattern ``@/*`` to ``src/*``, preserving the other paths information at run-time.

> **Please notice that paths are resolved relative to baseUrl.**

2. The next step is to update your vite configuration file, ``vite.config.ts`` file to the following.

```js
// ...other imports
import {resolve} from "path";

export default defineConfig(() => ({
	// ... other configurations
	resolve: {
		alias: {
			"@": resolve(__dirname, "src"),
		},
	}
}))
```
3. Now go to the file ``App.tsx`` and make the following changes

**Before:**
```js
import { useState } from "react";
import reactLogo from "./asset/react.svg";
import "./App.css";
```
**Now:**
```js
import { useState } from "react";
import reactLogo from "@/asset/react.svg";
import "@/App.css";
```

Your app should still be working properly. Thank you for reading thus far. You are free to explore other options. If this was helpful, do share and like.
