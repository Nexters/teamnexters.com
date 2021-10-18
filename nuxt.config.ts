import type { NuxtConfig } from "@nuxt/types";

const config: NuxtConfig = {
  target: "static",
  ssr: false,
  head: {
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
    ],
  },
  modules: ["@nuxt/content", "@nuxtjs/composition-api/module"],
  components: [
    "~/components",
    { path: "~/components/about", extensions: ["vue"] },
    { path: "~/components/project", extensions: ["vue"] },
    { path: "~/components/contact", extensions: ["vue"] },
    { path: "~/components/recruitment", extensions: ["vue"] },
  ],
  content: {
    nestedProperties: ["projects.idx"],
    extendParser: {
      ".custom": (file) => ({
        body: file.split("\n").map((line) => line.trim()),
      }),
    },
  },
  buildModules: ["@nuxt/typescript-build", "@nuxtjs/svg"],
  plugins: ["~/plugins/vue-mq"],
  css: [
    "~/assets/css/reset.css",
    "~/assets/css/webfont.css",
    "~/assets/css/_device.scss",
    "~/assets/css/setting.scss",
    "~/assets/css/color.scss",
    "~/assets/css/typography.scss",
  ],
  loading: "~/components/loading-bar.vue",
  router: {
    middleware: ["store"],
    // linkActiveClass: "nuxt-link-active",
  },
  pageTransition: {
    name: "my-page",
    mode: "out-in",
  },
};

export default config;
