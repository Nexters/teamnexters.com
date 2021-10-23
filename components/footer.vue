<template>
  <footer>
    <div class="footer">
      <div class="leftArea">
        <div class="sns">
          <ul v-for="item in items" :key="item.name">
            <a :href="item.href">
              <img :src="sns_icon[item.name]" :alt="item.name" />
            </a>
          </ul>
        </div>
        <div class="sponsor">
          <p @click="handleSponsorClick">
            sponsored
            <img class="arrow-right" :src="arrowIcon" />
          </p>
          <div v-if="isSponsorVisible" class="sponsorBox">
            <article class="sponsorList">
              <section class="sponsorItem">
                <span>Naver Cloud Platform</span>
              </section>
              <section class="sponsorItem">
                <span>Naver D2 </span>
              </section>
            </article>
          </div>
        </div>
      </div>
      <div class="copyrights">
        {{ copyrights }}
      </div>
    </div>
  </footer>
</template>

<script lang="ts">
import { defineComponent } from "@nuxtjs/composition-api";

export default defineComponent({
  name: "Footer",
  props: {
    items: {
      type: Array,
      required: true,
    },
    copyrights: {
      type: String,
      required: true,
    },
    isWhite: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  setup(props) {
    return {
      sns_icon: {
        facebook: props.isWhite
          ? require("~/assets/img/facebook.svg")
          : require("~/assets/img/facebook_black.svg"),
        github: props.isWhite
          ? require("~/assets/img/github.svg")
          : require("~/assets/img/github_black.svg"),
        instagram: props.isWhite
          ? require("~/assets/img/instagram.svg")
          : require("~/assets/img/instagram_black.svg"),
      },
      arrowIcon: props.isWhite
        ? require("~/assets/img/arrow_right.svg")
        : require("~/assets/img/arrow_right_black.svg"),
    };
  },
  data() {
    return {
      isSponsorVisible: false,
    };
  },
  methods: {
    handleSponsorClick() {
      this.isSponsorVisible = !this.isSponsorVisible;
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

footer {
  margin-top: auto;
}

.footer {
  .sponsor {
    position: relative;
    > p {
      display: flex;
      align-items: center;

      align-self: flex-end;
      font-style: normal;
      font-weight: normal;
      letter-spacing: -0.02em;
      opacity: 0.6;

      &:hover {
        cursor: pointer;
      }
    }
    .arrow-right {
      width: 16px;
      height: 16px;
    }
    .sponsorBox {
      position: absolute;
      bottom: 0;
      padding: 16px;
      border: 1px solid $grey02;
      border-radius: 8px;
      background-color: $white;

      .sponsorList {
        .sponsorItem {
          font-weight: 400;
          letter-spacing: -0.2;
          color: $grey03;
        }
      }
    }
  }
  .copyrights {
    align-self: flex-end;
    font-style: normal;
    font-weight: normal;
    text-align: center;
    letter-spacing: -0.02em;
    opacity: 0.6;
  }
  @include mobile {
    display: flex;
    margin-left: auto;
    flex-direction: column;
    padding: 0 0 24px 24px;
    .sns {
      display: flex;
      margin-right: auto;
      margin-bottom: 16px;
      img {
        height: 24px;
        width: 24px;
        opacity: 0.6;
      }
      ul {
        flex-direction: column;
        margin-right: 16px;
      }
    }
    .sponsor {
      > p {
        font-size: 14px;
        line-height: 21px;
      }
    }
    .copyrights {
      margin-right: auto;
      padding-top: 16px;

      font-size: 14px;
      line-height: 21px;
    }
    .sponsorBox {
      right: -60px;

      .sponsorItem {
        font-size: 12px;
        line-height: 18px;
      }
    }
  }
  @include tablet {
    display: flex;
    align-items: center;
    margin: auto;
    justify-content: center;
    padding: 0 64px 32px 64px;
    width: 713px;

    .sns {
      display: flex;
      margin-bottom: 24px;
      img {
        height: 32px;
        width: 32px;
        opacity: 0.6;
      }
      ul {
        flex-direction: column;
        margin-right: 32px;
      }
    }
    .sponsor {
      > p {
        font-size: 16px;
        line-height: 24px;
      }
    }
    .copyrights {
      margin-left: auto;

      font-size: 16px;
      line-height: 24px;
    }
    .sponsorBox {
      right: -75px;

      .sponsorItem {
        font-size: 14px;
        line-height: 21px;
      }
    }
  }
  @include desktop {
    display: flex;
    align-items: center;
    width: 1200px;
    margin: auto auto 32px auto;
    .sns {
      display: flex;
      margin-bottom: 24px;
      img {
        height: 32px;
        width: 32px;
        opacity: 0.6;
      }
      ul {
        flex-direction: column;
        margin-right: 32px;
      }
    }
    .sponsor {
      > p {
        font-size: 16px;
        line-height: 24px;
      }
    }
    .copyrights {
      margin-left: auto;

      font-size: 16px;
      line-height: 24px;
    }
    .sponsorBox {
      right: -75px;

      .sponsorItem {
        font-size: 14px;
        line-height: 21px;
      }
    }
  }
}
</style>
