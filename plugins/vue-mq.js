import Vue from "vue";
import VueMq from "vue-mq";

Vue.use(VueMq, {
  breakpoints: {
    mobile: 840,
    pc: 1920,
    other: Infinity,
  },
});
