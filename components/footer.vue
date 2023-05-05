<template>
  <footer>
    <div class="footer">
      <div class="footer-container">
        <div class="topArea">
          <div class="sponsor">
            <p @click="handleSponsorClick">
              Sponsored by
              <img class="arrow-right" :src="arrowIcon" />
            </p>
            <div class="sponsorBoxParagraph">
              <div v-if="isSponsorVisible" class="sponsorBox">
                <article class="sponsorList">
                  <section
                    v-for="sponsor in sponsors"
                    :key="sponsor.idx"
                    class="sponsorItem"
                  >
                    <a :href="sponsor.href">
                      <span>{{ sponsor.name }}</span>
                    </a>
                  </section>
                </article>
              </div>
            </div>
          </div>
          <div class="sns">
            <ul v-for="item in items" v-show="item.visible" :key="item.idx">
              <a :href="item.href">
                <img :src="icon(item)" :alt="item.name" />
              </a>
            </ul>
          </div>
        </div>
        <div class="sba-promotion" v-show="isShowSbaBanner">
          <img src="https://drive.google.com/uc?export=view&id=1Gtxu9vrt_tUDQCC_XXvDQhYXAmP4izCu" class="sba-img" size="100%" @click="linkToSeSacThon"/>
        </div>
        <div class="sponsorGuideText">
          본 페이지는 Naver Cloud Platform 서버 지원으로 운영되고 있습니다. @NEXTERS 2021
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
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
    sponsors: {
      type: Array,
      require: true,
    },
    isWhite: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  setup(props) {
    return {
      arrowIcon: props.isWhite
        ? require("~/assets/img/arrow_right.svg")
        : require("~/assets/img/arrow_right_black.svg"),
    };
  },
  data() {
    return {
      isSponsorVisible: false,
      isShowSbaBanner: this.$route.path !== '/',
    };
  },
  methods: {
    handleSponsorClick() {
      this.isSponsorVisible = !this.isSponsorVisible;
    },
    icon(item) {
      return this.isWhite ? item.white : item.black;
    },
    linkToSeSacThon() {
      window.location.href = "https://sesacthon-apply.goorm.io";
    }
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
  @include mobile {
    padding: 0 24px;
  }

  @include desktop {
    padding: 0 64px;
  }

  @include tablet {
    padding: 0 64px;
  }
}

.footer {
  margin: auto;
  width: 100%;
  letter-spacing: -0.02em;
  display: flex;
  flex-direction: column;
  .footer-container {
    display: flex;
    width: 100%;
    flex-direction: column;

    .sponsorGuideText {
      font-weight: 400;
      letter-spacing: -0.02em;
      opacity: 0.6;
      font-size: 14px;          
    }
  }

  .topArea {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    z-index: 1;
  }

  .sponsor {
    display: flex;
    margin-bottom: 24px;

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

    .sponsorBoxParagraph {
      position: relative;
      margin-left: 8px;
    }

    .sponsorBox {
      position: absolute;
      bottom: 0;
      padding: 15px;
      border: 1px solid $border-default;
      border-radius: 8px;
      background-color: $background-default;
      box-sizing: border-box;
      z-index: 10;

      .sponsorList {
        a {
          text-decoration: none;
          color: $text-sub;

          &:hover {
            text-decoration: underline;
          }
        }
        .sponsorItem {
          font-weight: 400;
          letter-spacing: -0.02em;
          color: $text-sub;
          margin-bottom: 8px;
        }
        .sponsorItem:last-child {
          margin-bottom: 0;
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
    max-width: 713px;
    margin-bottom: 24px;

    .sns {
      display: flex;
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
      margin-bottom: 16px;
      > p {
        font-size: 14px;
        line-height: 21px;
      }
    }
    .copyrights {
      align-self: flex-end;
      margin-left: auto;

      font-size: 14px;
      line-height: 21px;
    }
    .sponsorBox {
      width: 148px;

      .sponsorItem {
        font-size: 12px;
        line-height: 18px;
      }
    }
  }
  @include tablet {
    display: flex;
    align-items: center;
    justify-content: center;
    max-width: 1200px;
    margin-bottom: 32px;

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
      margin-bottom: 24px;
      > p {
        font-size: 18px;
        line-height: 27px;
      }
    }
    .copyrights {
      align-self: flex-end;
      margin-left: auto;

      font-size: 18px;
      line-height: 27px;
    }
    .sponsorBox {
      width: 168px;

      .sponsorItem {
        font-size: 14px;
        line-height: 21px;
      }
    }
  }
  @include desktop {
    display: flex;
    align-items: center;
    max-width: 1200px;
    margin-bottom: 32px;

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
        font-size: 18px;
        line-height: 27px;
      }
    }
    .copyrights {
      align-self: flex-end;
      margin-left: auto;

      font-size: 18px;
      line-height: 27px;
    }
    .sponsorBox {
      width: 168px;

      .sponsorItem {
        font-size: 14px;
        line-height: 21px;
      }
    }
  }

  .sba-promotion {
    width: 100%;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: start;
    grid-gap: 2.666666666666667vw;
    padding-bottom: 2.666666666666667vw;

    .sba-img {
      width: 378px;
      height: 164px;
      cursor: pointer;

      @include tablet {
        width: 35.26119402985075vw;
        height: 15.29850746268657vw;
      }

      @include mobile {
        width: 42.30769230769231vw;
        height: 18.35641025641026vw;
      }
    }
  }
}
</style>
