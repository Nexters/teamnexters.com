<template>
  <div class="contactBox" @click="onClick">
    <div class="leftArea">
      <img class="iconImage" :src="contact[contactType].icon" alt="imageName" />
      <p class="iconText">{{ contact[contactType].iconText }}</p>
    </div>
    <p class="text">{{ contact[contactType].text }}</p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "@nuxtjs/composition-api";

export default defineComponent({
  name: "ContactBox",
  props: {
    contactType: {
      type: String,
      require: false,
    },
    onClick: {
      type: Function,
      require: false,
    },
  },
  setup(props) {
    return {
      contact: {
        kakao: {
          icon: require("~/assets/img/kakao_16.svg"),
          iconText: "Kakao Channel",
          text: "@Nexters",
          link: "",
        },
        gmail: {
          icon: require("~/assets/img/gmail_16.svg"),
          iconText: "Gmail",
          text: "teamnexters@gmail.com",
          link: "",
        },
        facebook: {
          icon: require("~/assets/img/facebook_16.svg"),
          iconText: "Facebook",
          text: "@Nexterspage",
          link: "",
        },
      },
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

.contactBox {
  width: 100%;
  display: flex;
  flex-direction: row;
  font-weight: 700;
  background-color: $grey01;
  border-radius: 16px;
  justify-content: space-between;
  box-sizing: border-box;

  .leftArea {
    display: flex;
  }

  .text {
    color: $grey03;
    letter-spacing: -0.02em;
    font-weight: 400;
    align-self: center;
  }
}

@include d-c3 {
  .contactBox {
    font-size: 24px;
    line-height: 36px;
    padding: 32px;

    .iconText {
      margin-left: 16px;
    }

    .text {
      font-size: 18px;
      line-height: 27px;
    }

    &:hover {
      cursor: pointer;
    }
  }
}

@include d-c2 {
  .contactBox {
    font-size: 24px;
    line-height: 36px;
    padding: 32px;

    .text {
      font-size: 18px;
      line-height: 27px;
    }

    .iconText {
      margin-left: 16px;
    }
  }
}

@include d-c1 {
  .contactBox {
    font-size: 24px;
    line-height: 36px;
    padding: 32px;

    .iconText {
      margin-left: 16px;
    }

    .text {
      font-size: 18px;
      line-height: 27px;
    }
  }
}

@include m-c2 {
  .contactBox {
    font-size: 16px;
    line-height: 24px;
    padding: 24px;

    .iconText {
      margin-left: 8px;
    }

    .text {
      font-size: 14px;
      line-height: 21px;
    }
  }
}

@include m-c1 {
  .contactBox {
    font-size: 16px;
    line-height: 24px;
    padding: 24px;

    .iconText {
      margin-left: 8px;
    }

    .text {
      font-size: 14px;
      line-height: 21px;
    }
  }
}
</style>
