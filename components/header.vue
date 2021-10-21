<template>
  <nav class="navigation">
    <div :class="{ 'nav-header': true, overlay: isMenuOpen }">
      <nuxt-link to="/" class="logo" prefetch>
        <img
          :style="`display: ${isMenuOpen ? 'none' : 'block'}`"
          :src="img_logo"
          alt="NEXTERS_IMAGE_LOGO"
        />
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
        ? require("~/assets/img/nexters_img_logo.svg")
        : require("~/assets/img/nexters_img_logo_black.svg"),
      txt_logo: props.isWhite
        ? require("~/assets/img/nexters_txt_logo.svg")
        : require("~/assets/img/nexters_txt_logo_black.svg"),
      ic_menu: props.isWhite
        ? require("~/assets/img/ic_menu.svg")
        : require("~/assets/img/ic_menu_black.svg"),
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
@import "~/assets/css/setting.scss";

* {
  font-family: Spoqa Han Sans Neo;
}

.navigation {
  background: transparent;
  position: absolute;
  width: 100%;
}

nav {
  z-index: 999;
  display: flex;
  align-items: center;
  height: 73px;
  .header-item {
    padding: 0 48.5px 0 0;
    font-size: 24px;
    font-style: normal;
    font-weight: bold;
    line-height: 36px;
    letter-spacing: -0.02em;
    color: $black;
    text-decoration: none;
  }
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
      position: fixed;
      top: 73px;
      left: 0;
      right: 0;
      bottom: 0;
      padding-top: 32px;
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
    .header-item:last-child {
      padding: 0;
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
    .header-item:last-child {
      padding: 0;
    }
  }

  .white-font {
    color: $white;
  }
}

@include desktop {
  a.nuxt-link-active {
    text-decoration: underline;
    text-underline-position: under;
  }
}

@include tablet {
  a.nuxt-link-active {
    text-decoration: underline;
    text-underline-position: under;
  }
}

@include mobile {
  a.nuxt-link-active {
    text-decoration: none;
    color: $grey03 !important;
  }
}
</style>
