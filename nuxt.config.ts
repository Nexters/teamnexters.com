import type { NuxtConfig } from "@nuxt/types";

const config: NuxtConfig = {
  target: "static",
  head:{
    meta:[{charset: 'utf-8'}, {name: 'viewport', content: 'width=device-width, initial-scale=1'}]
  },
  modules: ["@nuxt/content"],
  components: true,
  content: {
    nestedProperties: ["a.b"],
    extendParser: {
      ".custom": (file) => ({
        body: file.split("\n").map((line) => line.trim()),
      }),
    },
  },
  buildModules: ["@nuxt/typescript-build"],
  plugins: ["~/plugins/composition-api"],
  css:["~/assets/css/reset.css", "~/assets/css/webfont.css", "~/assets/css/_device.scss"],
  // image:{
  //   facebook: "~/assets/img/facebook.png",
  //   github: "~/assets/img/github.png",
  //   instagram: "~/assets/img/instagram.png",
  // },
};

export default config;
