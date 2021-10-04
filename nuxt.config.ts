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
  modules: ["@nuxt/content"],
  components: [
    "~/components",
    { path: "~/components/about", extensions: ["vue"] },
    { path: "~/components/project", extensions: ["vue"] },
  ],
  content: {
    nestedProperties: ["projects.idx"],
    extendParser: {
      ".custom": (file) => ({
        body: file.split("\n").map((line) => line.trim()),
      }),
    },
  },
  buildModules: ["@nuxt/typescript-build"],
  plugins: ["~/plugins/composition-api"],
  css: [
    "~/assets/css/reset.css",
    "~/assets/css/webfont.css",
    "~/assets/css/_device.scss",
  ],
  loading: "~/components/loading-bar.vue",
};

export default config;
