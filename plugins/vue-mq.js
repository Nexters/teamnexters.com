import Vue from "vue";
import VueMq from "vue-mq";

const pageTitle = {
  watch: {
    vuePageTitle() {
      document.title = `Nexters`;
    },
  },
};

Vue.mixin(pageTitle);
Vue.use(VueMq, {
  breakpoints: {
    mobile: 840,
    pc: 1200,
    other: Infinity,
  },
  defaultBreakPoint: "mobile",
});
