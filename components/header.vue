<template>
  <nav>
    <div :class="{ 'nav-header': true, overlay: isMenuOpen }">
      <nuxt-link to="/" class="logo" prefetch>
        <img :src="img_logo" alt="NEXTERS_IMAGE_LOGO" />
        <img class="text-logo" :src="txt_logo" alt="NEXTERS_TEXT_LOGO" />
      </nuxt-link>
      <div class="menu" @click="toggleMenu">
        <img v-if="isMenuOpen" :src="ic_close" alt="ic_close" />
        <img v-else :src="ic_menu" alt="ic_menu" />
      </div>
    </div>
    <div
      class="menu-items"
      :class="{ 'menu-close': !isMenuOpen, overlay: isMenuOpen }"
    >
      <nuxt-link
        v-for="header in headers"
        :key="header.name"
        :to="header.href"
        :class="{ 'header-item': true, 'white-font': isWhite }"
      >
        {{ header.name }}
      </nuxt-link>
    </div>
  </nav>
</template>

<script>
import { defineComponent, useStore, computed } from "@nuxtjs/composition-api";
export default defineComponent({
  name: "Header",

  props: {
    headers: {
      type: Array,
      required: true,
    },
    isWhite: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  setup(props) {
    const store = useStore();
    return {
      toggleMenu: () => {
        store.dispatch("toggleMenu");
      },
      isMenuOpen: computed(() => store.state.isMenuOpen),
      img_logo: props.isWhite
        ? require("~/assets/img/nexters_img_logo.png")
        : require("~/assets/img/nexters_img_logo_black.png"),
      txt_logo: props.isWhite
        ? require("~/assets/img/nexters_txt_logo.png")
        : require("~/assets/img/nexters_txt_logo_black.png"),
      ic_menu: props.isWhite
        ? require("~/assets/img/ic_menu.png")
        : require("~/assets/img/ic_menu_black.png"),
      ic_close: props.isWhite
        ? require("~/assets/img/ic_close.svg")
        : require("~/assets/img/ic_close.svg"),
    };
  },
  data() {
    return {
      menuClose: true,
    };
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
* {
  font-family: Spoqa Han Sans Neo;
}
.nuxt-link-active {
  color: red;
}
nav {
  z-index: 999;
  display: flex;
  align-items: center;
  height: 73px;
  @include mobile {
    flex-direction: column;
    .overlay {
      background-color: white;
      .white-font {
        color: black;
      }
      .header-item {
        padding-left: 24px;
        font-weight: bold;
        font-size: 32px;
        line-height: 48px;
        letter-spacing: -0.02em;
      }
    }
    .menu-items {
      width: 100%;
      position: absolute;
      top: 73px;
      padding-top: 32px;
      height: 100%;
      display: flex;
      flex-direction: column;
      gap: 32px;
    }

    .nav-header {
      height: 100%;
      width: 100%;
      display: flex;
      .logo {
        display: flex;
        align-items: center;
        height: 73px;
        margin: auto auto auto 16px;
      }
      .menu {
        width: 24px;
        height: 24px;
        margin: auto 16px auto auto;
        display: block;
        cursor: pointer;
      }
    }
    .text-logo {
      display: none;
    }
    .menu-close {
      display: none;
    }
  }
  @include tablet {
    flex-direction: column;
    .overlay {
      background-color: white;
      .white-font {
        color: black;
      }
      .header-item {
        padding-left: 24px;
        font-weight: bold;
        font-size: 32px;
        line-height: 48px;
        letter-spacing: -0.02em;
      }
    }
    .menu-items {
      width: 100%;
      position: absolute;
      top: 73px;
      padding-top: 32px;
      height: 100%;
      display: flex;
      flex-direction: column;
      gap: 32px;
    }
    .nav-header {
      width: 100%;
      display: flex;
      .logo {
        display: flex;
        align-items: center;
        height: 73px;
        margin: auto auto auto 16px;
      }
      .menu {
        width: 24px;
        height: 24px;
        margin: auto 16px auto auto;
        display: block;
        cursor: pointer;
      }
    }
    .text-logo {
      display: none;
    }
    .menu-close {
      display: none;
    }
  }
  @include desktop {
    .nav-header {
      height: 73px;
    }
    .menu {
      display: none;
    }
    .logo {
      height: 73px;
      padding: 0 48.5px 0 24px;
      display: flex;
      align-items: center;
      img {
        padding-right: 7px;
      }
    }
  }

  .header-item {
    padding: 0 48.5px 0 0;
    font-size: 24px;
    font-style: normal;
    font-weight: bold;
    line-height: 36px;
    letter-spacing: -0.02em;
    color: #000000;
    text-decoration: none;
  }
  .white-font {
    color: #ffffff;
  }
}
</style>
