import type { NuxtConfig } from "@nuxt/types";

const config: NuxtConfig = {
  publicRuntimeConfig: { baseURL: process.env.NUXT_BASE_URL },
  target: "static",
  ssr: false,
  head: {
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      {
        hid: "description",
        name: "description",
        content:
          "IT 연합동아리 넥스터즈(NEXTERS)는 IT 생태계의 주인공인 개발자와 디자이너들을 위한 모임입니다. 재능있는 디자이너와 개발자들이 함께 모여 자유로운 분위기에서 어울리고 도움을 주고받으며 협업을 통해 원하는 애플리케이션을 만드는 모임입니다.",
      },
      {
        hid: "title",
        name: "title",
        content: "NEXTERS | 개발자와 디자이너를 위한 IT 연합동아리",
      },
      {
        hid: "og-image",
        property: "og:image",
        name: "og:image",
        content: "http://teamnexters.com/img/20th/09_Homepage_favicon.ico",
      },
      {
        hid: "og-title",
        property: "og:title",
        name: "og:title",
        content: "NEXTERS | Network for Experts",
      },
      {
        hid: "og-description",
        property: "og:description",
        name: "og:description",
        content:
          "IT 연합동아리 넥스터즈(NEXTERS)는 IT 생태계의 주인공인 개발자와 디자이너들을 위한 모임입니다. 재능있는 디자이너와 개발자들이 함께 모여 자유로운 분위기에서 어울리고 도움을 주고받으며 협업을 통해 원하는 애플리케이션을 만드는 모임입니다.",
      },
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
