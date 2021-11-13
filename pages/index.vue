<template>
  <div class="main-container">
    <transition name="main">
      <div class="slogan">
        <p class="title">{{ slogan }}</p>
        <div class="description">
          <p>{{ description }}</p>
          <Badge v-show="is_recruiting" :text="badge_text" />
        </div>
        <div class="quick-link">
          <ArrowButton :href="link_href" :text="link_text" :size="link_size" />
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import { defineComponent } from "@nuxtjs/composition-api";

export default defineComponent({
  name: "Main",
  layout: "main",
  transition: {
    name: "main",
  },
  setup() {
    return {};
  },
  async asyncData({ $content }) {
    const main = await $content("main")
      .only([
        "slogan",
        "default_desc",
        "default_a",
        "default_href",
        "th",
        "recruitment_notice",
        "recruitment_start",
        "recruitment_deadline",
        "recruitment_notice_a",
        "recruitment_notice_desc",
        "recruitment_in_progress_a",
        "recruitment_in_progress_desc",
        "recruitment_href",
      ])
      .fetch();
    const {
      slogan,
      default_desc,
      default_a,
      default_href,
      th,
      recruitment_notice,
      recruitment_start,
      recruitment_deadline,
      recruitment_notice_a,
      recruitment_notice_desc,
      recruitment_in_progress_a,
      recruitment_in_progress_desc,
      recruitment_href,
    } = main;
    return {
      slogan: slogan,
      default_desc: default_desc,
      default_a: default_a,
      default_href: default_href,
      th: th,
      recruitment_notice: recruitment_notice,
      recruitment_start: recruitment_start,
      recruitment_deadline: recruitment_deadline,
      recruitment_notice_a: recruitment_notice_a,
      recruitment_notice_desc: recruitment_notice_desc,
      recruitment_in_progress_a: recruitment_in_progress_a,
      recruitment_in_progress_desc: recruitment_in_progress_desc,
      recruitment_href: recruitment_href,
    };
  },
  computed: {
    link_size() {
      return this.$mq === "mobile" ? 16 : 24;
    },
    link_text() {
      let result = this.default_a;
      if (this.before_recruitment) {
        result = `${this.th}기 ${this.recruitment_notice_a}`;
      } else if (this.is_recruiting) {
        result = `${this.th}기 ${this.recruitment_in_progress_a}`;
      }

      return result;
    },
    link_href() {
      let result = this.default_href;
      if (this.before_recruitment) {
        result = this.recruitment_href;
      } else if (this.is_recruiting) {
        result = this.recruitment_href;
      }
      return result;
    },
    description() {
      let desc = this.default_desc;
      if (this.before_recruitment) {
        let date = new Date(this.recruitment_start);
        desc =
          `${date.getMonth() + 1}월 ${date.getDate()}일` +
          ` 넥스터즈 ${this.th}기 ${this.recruitment_notice_desc}`;
      } else if (this.is_recruiting) {
        desc = `현재 넥스터즈 ${this.th}기 ${this.recruitment_in_progress_desc}`;
      }
      return desc;
    },
    badge_text() {
      return this.d_day > 0 ? `마감 D-${this.d_day}` : "마감 D-day";
    },
    notice_day() {
      const result = new Date(this.recruitment_notice) - new Date();
      return Math.ceil(result / 86400000);
    },
    s_day() {
      const result = new Date(this.recruitment_start) - new Date();
      return Math.ceil(result / 86400000);
    },
    d_day() {
      const result = new Date(this.recruitment_deadline) - new Date();
      return this.s_day < 0 ? Math.ceil(result / 86400000) : 0;
    },
    before_recruitment() {
      return this.notice_day < 0 && this.s_day >= 0;
    },
    is_recruiting() {
      return this.s_day < 0 && this.d_day >= 0;
    },
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
@import "~/assets/css/setting.scss";

* {
  font-family: Spoqa Han Sans Neo;
}

.main-enter-active,
.main-leave-active {
  transition: opacity 1.5s;
}
.main-enter,
.main-leave-active {
  opacity: 0;
}
a {
  text-decoration: none;
  color: $text-inverse;
}

.main-container {
  width: 100%;
  height: 100vh;
  color: $text-inverse;
  display: flex;
  margin: auto;
  padding-top: 73px;

  align-items: center;

  .slogan {
    margin: auto;
    width: 100%;
  }

  @include mobile {
    .slogan {
      max-width: 713px;
      padding: 0 24px;

      .title {
        font-family: "Montserrat", sans-serif;
        white-space: pre-wrap;
        font-style: normal;
        font-weight: 800;
        font-size: 40px;
        line-height: 48.76px;
      }
      .description {
        display: flex;
        align-items: center;
        margin-top: 16px;

        p {
          font-style: normal;
          font-weight: normal;
          font-size: 16px;
          line-height: 24px;
          letter-spacing: -0.02em;
          margin-right: 8px;
        }
      }
      .quick-link {
        display: flex;
        flex-direction: row;
        align-items: center;
        align-content: center;
        padding-top: 40px;

        a {
          display: flex;
          font-style: normal;
          font-weight: bold;
          font-size: 16px;
          line-height: 24px;
          letter-spacing: -0.02em;
        }

        img {
          width: 16px;
          height: 16px;
          margin: auto 0 auto 8px;
        }
      }
    }
  }
  @include tablet {
    .slogan {
      max-width: 1200px;
      padding: 0 64px;
      .title {
        font-family: "Montserrat", sans-serif;
        white-space: pre-wrap;
        font-style: normal;
        font-weight: 900;
        font-size: 90px;
        line-height: 110px;
      }
      .description {
        display: flex;
        align-items: center;
        margin-top: 32px;
        p {
          font-style: normal;
          font-weight: normal;
          font-size: 24px;
          line-height: 36px;
          letter-spacing: -0.02em;
          margin-right: 20px;
        }
      }
      .quick-link {
        display: flex;
        flex-direction: row;
        align-content: center;
        padding-top: 86px;
        a {
          display: flex;
          font-style: normal;
          font-weight: bold;
          font-size: 24px;
          line-height: 24px;
          letter-spacing: -0.02em;
        }

        img {
          width: 24px;
          height: 24px;
          margin: auto 0 auto 8px;
        }
      }
    }
  }
  @include desktop {
    .slogan {
      max-width: 1200px;
      padding: 0 64px;
      .title {
        font-family: "Montserrat", sans-serif;
        white-space: pre-wrap;
        font-style: normal;
        font-weight: 900;
        font-size: 90px;
        line-height: 110px;
      }
      .description {
        display: flex;
        align-items: center;
        margin-top: 32px;
        p {
          font-style: normal;
          font-weight: normal;
          font-size: 24px;
          line-height: 36px;
          letter-spacing: -0.02em;
          margin-right: 20px;
        }
      }
      .quick-link {
        display: flex;
        flex-direction: row;
        align-content: center;
        padding-top: 86px;
        a {
          display: flex;
          font-style: normal;
          font-weight: bold;
          font-size: 24px;
          line-height: 24px;
          letter-spacing: -0.02em;
        }

        img {
          width: 24px;
          height: 24px;
          margin: auto 0 auto 8px;
        }
      }
    }
  }
}
</style>
