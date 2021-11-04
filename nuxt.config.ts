import type { NuxtConfig } from "@nuxt/types";

const config: NuxtConfig = {
  publicRuntimeConfig: { baseURL: process.env.NUXT_BASE_URL },
  target: "static",
  ssr: false,
  head: {
    link: [{ rel: "icon", type: "image/x-icon", href: "/favicon_N20_02.png" }],
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      {
        hid: "title",
        name: "title",
        content: "NEXTERS : IT Community for Experts",
      },
      {
        hid: "og-image",
        property: "og:image",
        name: "og:image",
        content: "/og-image.png",
      },
      {
        hid: "og-title",
        property: "og:title",
        name: "og:title",
        content: "NEXTERS : IT Community for Experts",
      },
    ],
  },
  modules: [
    "@nuxt/content",
    "@nuxtjs/composition-api/module",
    [
      "nuxt-lazy-load",
      {
        // These are the default values
        images: true,
        videos: true,
        audios: true,
        iframes: true,
        native: false,
        directiveOnly: false,

        // Default image must be in the static folder
        defaultImage: "/no-image.svg",

        // To remove class set value to false
        loadingClass: "isLoading",
        loadedClass: "isLoaded",
        appendClass: "lazyLoad",

        observerConfig: {
          // See IntersectionObserver documentation
        },
      },
    ],
  ],
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
    middleware: ["store", "trailingSlashRedirect"],
    // linkActiveClass: "nuxt-link-active",
    trailingSlash: false,
  },
  pageTransition: {
    name: "my-page",
    mode: "out-in",
  },
};

export default config;
