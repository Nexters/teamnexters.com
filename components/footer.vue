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
import { defineComponent } from "@vue/composition-api";

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
          ? require("~/assets/img/facebook.png")
          : require("~/assets/img/facebook_black.png"),
        github: props.isWhite
          ? require("~/assets/img/github.png")
          : require("~/assets/img/github_black.png"),
        instagram: props.isWhite
          ? require("~/assets/img/instagram.png")
          : require("~/assets/img/instagram_black.png"),
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
    }
  }
  @include tablet {
    display: flex;
    align-items: center;
    width: calc(100% - 64px);
    margin: auto auto 32px auto;
    justify-content: center;

    .sns {
      display: flex;
      img {
        height: 32px;
        width: 32px;
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
      }
      ul {
        flex-direction: column;
        margin-right: 32px;
      }
    }
    .copyrights {
      margin-left: auto;
      padding-right: 64px;

      font-style: normal;
      font-weight: normal;
      font-size: 16px;
      line-height: 24px;
      text-align: center;
      letter-spacing: -0.02em;
    }
  }
}
</style>
