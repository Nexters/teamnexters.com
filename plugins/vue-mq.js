import Vue from "vue";
import VueMq from "vue-mq";

Vue.use(VueMq, {
  breakpoints: {
    mobile: 840,
    pc: 1200,
    other: Infinity,
  },
  defaultBreakPoint: "mobile",
});
