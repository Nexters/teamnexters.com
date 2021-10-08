<template>
  <div class="contactBox">
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
* {
  font-family: Spoqa Han Sans Neo;
}

.contactBox {
  width: 100%;
  display: flex;
  flex-direction: row;
  font-weight: 700;
  background-color: #f6f6f6;
  border-radius: 16px;
  justify-content: space-between;
  box-sizing: border-box;

  .leftArea {
    display: flex;
  }

  .text {
    color: #777777;
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
  }
}

@include d-c2 {
  .contactBox {
    font-size: 24px;
    line-height: 36px;
    padding: 32px;

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
  }
}
</style>
