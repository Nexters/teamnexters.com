<template>
  <footer>
    <div class="footer">
      <div class="sns">
        <ul v-for="item in items" :key="item.name">
          <a :href="item.href">
            <img :src="sns_icon[item.name]" :alt="item.name" />
          </a>
        </ul>
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
    };
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";

* {
  font-family: Spoqa Han Sans Neo;
}

footer {
  margin-top: auto;
}

.footer {
  @include mobile {
    display: flex;
    margin-left: auto;
    flex-direction: column;
    padding: 0 0 24px 24px;
    .sns {
      display: flex;
      margin-right: auto;
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
    .copyrights {
      margin-right: auto;
      padding-top: 16px;

      font-style: normal;
      font-weight: normal;
      font-size: 14px;
      line-height: 21px;
      text-align: center;
      letter-spacing: -0.02em;
      opacity: 0.6;
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
    .copyrights {
      margin-left: auto;

      font-style: normal;
      font-weight: normal;
      font-size: 16px;
      line-height: 24px;
      text-align: center;
      letter-spacing: -0.02em;
      opacity: 0.6;
    }
  }
  @include desktop {
    display: flex;
    align-items: center;
    width: 1200px;
    margin: auto auto 32px auto;
    .sns {
      display: flex;
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
    .copyrights {
      margin-left: auto;

      font-style: normal;
      font-weight: normal;
      font-size: 16px;
      line-height: 24px;
      text-align: center;
      letter-spacing: -0.02em;
      opacity: 0.6;
    }
  }
}
</style>
