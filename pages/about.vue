<template>
  <transition name="about" mode="out-in">
    <div class="about-container">
      <div class="slogan">
        <h1 class="slogan-text">{{ slogan }}</h1>
      </div>
      <div class="info-table">
        <div class="info-row">
          <h2 class="title">{{ info.title }}</h2>
          <div class="information">
            <div class="cards">
              <!-- <pre>{{ informations }}</pre> -->
              <InfoCard
                v-for="item in info.items"
                :key="item.title"
                :title="item.title"
                :value="item.value"
                :description="item.description"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="contents">
        <!-- horizontal scroll -->
        <div class="activity-row">
          <div class="activities">
            <h2 class="title">{{ act.title }}</h2>
            <h3 class="desc">{{ act.desc }}</h3>
            <div class="cards">
              <ActivityCard
                v-for="item in act.items"
                :key="item.title"
                :description="item.description"
                :title="item.title"
                :thumbnail="item.thumbnail"
              />
            </div>
          </div>
        </div>
        <div class="review-row">
          <div class="reviews">
            <h2 class="title">{{ review.title }}</h2>
            <div class="cards">
              <ReviewCard
                v-for="item in review.items"
                :key="item.id"
                :th="item.th"
                :title="item.title"
                :author="item.author"
                :href="item.href"
              />
            </div>
            <div v-show="isRemain" class="more">
              <div class="lead-more" @click="onClickMore">
                <p>Load more</p>
                <img src="~/assets/img/ic_down.svg" alt="" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { defineComponent } from "@nuxtjs/composition-api";
import { mapGetters, mapActions } from "vuex";
export default defineComponent({
  name: "AboutPage",
  transition: {
    name: "about",
  },
  async asyncData({ $content }) {
    const {
      slogan,
      info_title,
      info_desc,
      activity_title,
      activity_desc,
      review_title,
      review_desc,
    } = await $content("about/text")
      .only([
        "slogan",
        "info_title",
        "info_desc",
        "activity_title",
        "activity_desc",
        "review_title",
        "review_desc",
      ])
      .fetch();
    const informations = await $content("about/informations")
      .only(["title", "value", "description"])
      .fetch();
    const activities = await $content("about/activities")
      .only(["description", "title", "thumbnail"])
      .fetch();
    const { length: total } = await $content("about/reviews").fetch();
    const reviews = await $content("about/reviews")
      .only(["id", "th", "title", "author", "href"])
      .sortBy("id", "desc")
      .limit(6)
      .fetch()
      .catch((err) => {
        console.log(err);
      });
    return {
      slogan: slogan,
      info: {
        title: info_title,
        desc: info_desc,
        items: informations,
      },
      act: {
        title: activity_title,
        desc: activity_desc,
        items: activities,
      },
      review: {
        title: review_title,
        desc: review_desc,
        total: total,
        items: reviews,
        more: true,
      },
    };
  },
  data() {
    return {
      slogan: "",
      info: {
        title: "",
        items: [],
      },
      act: {
        title: "",
        description: "",
        items: [],
      },
      review: {
        title: "",
        total: 0,
        items: [],
        more: true,
      },
    };
  },
  computed: {
    ...mapGetters({
      reviewLimitFromStore: "about/reviewLimit",
    }),
    reviewLimit: {
      get() {
        return this.reviewLimitFromStore;
      },
      set(limit) {
        return this.setReviewLimit(limit);
      },
    },
    isRemain: {
      get() {
        return this.reviewLimit < this.review.total;
      },
    },
  },
  methods: {
    ...mapActions({
      setReviewLimit: "about/reviewLimit",
    }),
    async onClickMore() {
      if (this.isRemain) {
        this.reviewLimit += 6;
      } else {
        this.reviewLimit = this.review.total;
        this.review.more = false;
      }
      const reviews = await this.$content("about/reviews")
        .only(["id", "th", "title", "author", "href"])
        .sortBy("id", "desc")
        .limit(this.reviewLimit)
        .fetch()
        .catch((err) => {
          console.log(err);
        });
      this.review.items = reviews;
    },
  },
  fetchOnServer: false,
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
@import "~/assets/css/setting.scss";
@import "~/assets/css/about-top-image.scss";

* {
  font-family: Spoqa Han Sans Neo;
}
.about-enter-active,
.about-leave-active {
  transition: opacity 1.5s;
}
.about-enter,
.about-leave-active {
  opacity: 0;
}

.slogan {
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;

  padding-top: 73px;
}

.about-container {
  @include desktop {
    .contents {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      width: 100%;
      margin: 0 auto 0 auto;
    }
    .slogan {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      width: 100%;
      height: 809px;
      background-image: $about-desktop;
      margin-bottom: 120px;
      h1 {
        width: 1200px;
        white-space: pre-wrap;
        font-style: normal;
        font-weight: normal;
        font-size: 24px;
        line-height: 36px;

        text-align: center;
        letter-spacing: -0.02em;

        color: $text-sub;
      }
    }
    .title {
      font-style: normal;
      font-weight: bold;
      font-size: 48px;
      line-height: 64px;
      letter-spacing: -0.02em;
      white-space: pre-wrap;

      color: $text-default;
    }
    .info-table {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-bottom: 120px;
      .info-row {
        display: flex;
        flex-direction: column;
        justify-content: center;
      }
      .information {
        margin-top: 42px;
        width: 1200px;
        display: flex;
        flex-direction: column;
        .cards {
          display: flex;
          justify-content: space-between;
        }
      }
    }
    .activity-row {
      display: flex;
      justify-content: center;
      margin-bottom: 120px;
    }
    .activities {
      display: flex;
      flex-direction: column;
      width: 1200px;
      grid-gap: 32px;
      .desc {
        font-style: normal;
        font-weight: normal;
        font-size: 24px;
        line-height: 36px;
        letter-spacing: -0.02em;
        white-space: pre-wrap;
        color: $text-default;
      }
      .cards {
        display: flex;
        flex-direction: row;
        box-sizing: border-box;
        flex-wrap: wrap;
        grid-gap: 32px;
      }
    }
    .review-row {
      display: flex;
      justify-content: center;
    }
    .reviews {
      display: flex;
      flex-direction: column;
      width: 1200px;
      margin-bottom: 120px;
      .cards {
        margin-top: 48px;
        display: flex;
        flex-direction: row;
        box-sizing: border-box;
        flex-wrap: wrap;
        grid-gap: 32px;
      }
      .more {
        margin-top: 48px;
        display: flex;
        flex-direction: column;
        align-items: center;
        .lead-more {
          display: flex;
          justify-content: space-between;
          align-items: center;
          width: 155px;
          height: 68px;
          cursor: pointer;
          font-style: normal;
          font-weight: bold;
          font-size: 24px;
          line-height: 36px;
          letter-spacing: -0.02em;
          color: $text-default;
        }
      }
    }
  }
  @include tablet {
    .contents {
      display: flex;
      flex-direction: column;
      width: calc(100% - 128px);
      margin: 0 auto 0 auto;
      padding: 0 64px 0 64px;
    }
    .slogan {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      height: 809px;
      background: $about-desktop;
      margin-bottom: 120px;
      .slogan-text {
        white-space: pre-wrap;
        font-style: normal;
        font-weight: normal;
        font-size: 24px;
        line-height: 36px;

        text-align: center;
        letter-spacing: -0.02em;

        color: $text-sub;
      }
    }
    .title {
      font-style: normal;
      font-weight: bold;
      font-size: 48px;
      line-height: 64px;
      letter-spacing: -0.02em;
      white-space: pre-wrap;

      color: $text-default;
    }
    .info-table {
      .info-row {
        display: flex;
        flex-direction: column;
        margin-bottom: 120px;
        .title {
          padding-left: 64px;
        }
        .information {
          margin-top: 48px;
          overflow-x: auto;
          scrollbar-width: none;
          -ms-overflow-style: none;
          -webkit-overflow-scrolling: touch;
          &::-webkit-scrollbar {
            display: none;
          }
          display: flex;
          flex-direction: column;
          .cards {
            min-width: 1200px;
            // grid-gap: 32px;
            justify-content: space-between;
            display: inline-flex;
            flex: 0 0 auto;
            padding: 0 64px 0 64px;
          }
        }
      }
    }
    .activity-row {
      display: flex;
    }
    .activities {
      display: flex;
      flex-direction: column;
      grid-gap: 32px;
      .desc {
        font-style: normal;
        font-weight: normal;
        font-size: 16px;
        line-height: 24px;
        letter-spacing: -0.02em;
        white-space: pre-wrap;
        color: $text-default;
      }
      .cards {
        display: flex;
        flex-direction: row;
        box-sizing: border-box;
        flex-wrap: wrap;
        grid-gap: 32px;
      }
    }
    .review-row {
      display: flex;
      justify-content: center;
      margin-top: 120px;
    }
    .reviews {
      display: flex;
      flex-direction: column;
      margin-bottom: 120px;
      .cards {
        margin-top: 32px;
        display: flex;
        flex-direction: row;
        box-sizing: border-box;
        flex-wrap: wrap;
        grid-gap: 32px;
      }
      .more {
        margin-top: 48px;
        display: flex;
        flex-direction: column;
        align-items: center;
        .lead-more {
          display: flex;
          justify-content: space-between;
          align-items: center;
          width: 155px;
          height: 68px;
          cursor: pointer;
          font-style: normal;
          font-weight: bold;
          font-size: 24px;
          line-height: 36px;
          letter-spacing: -0.02em;
          color: $text-default;
        }
      }
    }
  }
  @include mobile {
    .contents {
      display: flex;
      flex-direction: column;
      width: calc(100% - 48px);
      margin: 0 auto 0 auto;
      padding: 0 24px 0 24px;
    }
    .slogan {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      height: 484px;
      background: $about-mobile;
      margin-bottom: 64px;
      .slogan-text {
        white-space: pre-wrap;
        font-style: normal;
        font-weight: normal;
        font-size: 16px;
        line-height: 24px;
        text-align: center;
        letter-spacing: -0.02em;

        color: $text-sub;
      }
    }
    .title {
      font-style: normal;
      font-weight: bold;
      font-size: 32px;
      line-height: 48px;
      letter-spacing: -0.02em;
      white-space: pre-wrap;

      color: $text-default;
    }
    .info-table {
      .info-row {
        display: flex;
        flex-direction: column;
        margin-bottom: 64px;
        .title {
          padding-left: 24px;
        }
        .information {
          margin-top: 24px;
          overflow-x: auto;
          scrollbar-width: none;
          -ms-overflow-style: none;
          -webkit-overflow-scrolling: touch;
          &::-webkit-scrollbar {
            display: none;
          }
          display: flex;
          flex-direction: column;
          .cards {
            min-width: 752px;
            justify-content: space-between;
            display: inline-flex;
            flex: 0 0 auto;
            padding: 0 24px 0 24px;
          }
        }
      }
    }
    .activities {
      margin-bottom: 64px;
      display: flex;
      flex-direction: column;
      width: 100%;
      .desc {
        margin-top: 16px;
        font-style: normal;
        font-weight: normal;
        font-size: 16px;
        line-height: 24px;
        letter-spacing: -0.02em;
        white-space: pre-wrap;
        color: $text-default;
      }
      .cards {
        margin-top: 16px;
        display: flex;
        justify-content: space-between;
        flex-direction: column;
        // grid-gap: 16px;
        > div {
          margin-bottom: 16px;
        }
        > div:last-child {
          margin-bottom: 0;
        }
      }
    }
    .reviews {
      display: flex;
      flex-direction: column;
      margin-bottom: 64px;
      .cards {
        margin-top: 16px;
        display: flex;
        flex-direction: row;
        box-sizing: border-box;
        flex-wrap: wrap;
        justify-content: space-between;
        > div {
          margin-bottom: 16px;
        }
        > div:last-child {
          margin-bottom: 0;
        }
      }
      .more {
        margin-top: 24px;
        display: flex;
        flex-direction: column;
        align-items: center;
        .lead-more {
          display: flex;
          justify-content: space-between;
          align-items: center;
          width: 106px;
          height: 40px;
          cursor: pointer;
          font-style: normal;
          font-weight: bold;
          font-size: 16px;
          line-height: 24px;
          letter-spacing: -0.02em;
          color: $text-default;
          img {
            width: 13.33px;
            height: 7.33px;
          }
        }
      }
    }
  }
}
</style>
