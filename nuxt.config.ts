import type { NuxtConfig } from "@nuxt/types";

const config: NuxtConfig = {
  target: "static",
  modules: ["@nuxt/content"],
  components: true,
  content: {
    nestedProperties: ["categories.slug"],
    extendParser: {
      ".custom": (file) => ({
        body: file.split("\n").map((line) => line.trim()),
      }),
    },
  },
  buildModules: ["@nuxt/typescript-build"],
  plugins: ["~/plugins/composition-api", "~/plugins/vue-mq"],
  css:["~/assets/css/reset.css"]
};

export default config;
