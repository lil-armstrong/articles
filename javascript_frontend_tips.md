<!-- javascript_frontend_tips.md -->

CSS Escaping
CSS injection can be unobvious and have bad repercussions. Some IE versions even execute arbitrary JavaScript within url declarations. At the time of writing this, there is an upcoming standard to sanitize CSS from JavaScript, CSS.escape. It's not very well supported across browsers yet, so we recommend using the [polyfill by Mathias Bynens](https://github.com/mathiasbynens/CSS.escape) in your app. Install using the following:

```bash
yarn add css.escape
```

UI libraries to use
- [ChakraUI](https://chakra-ui.com/)
- [Mantine](https://mantine.dev/styles/sx/)
- [Material UI](https://mui.com)

Tooling
- Vitest
- Create React

Frameworks
- Nextjs
- Nuxtjs


