<template>
  <div class="noticeBox">
    <h2 class="contentTitle">
      <img class="noticeIcon" src="~/assets/img/ic_caution.svg" />{{ boxTitle }}
    </h2>
    <p v-for="content in contents" :key="content.id" class="content">
      <span class="dot" />{{ content.notice }}
    </p>
  </div>
</template>

<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "NoticeBox",
  props: {
    boxTitle: {
      type: String,
      require: true,
    },
    contents: {
      type: Array,
      require: true,
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

.noticeBox {
  background-color: $background-sub;
  border: 1px solid $border-default;

  .contentTitle {
    font-weight: 700;

    .noticeIcon {
      vertical-align: top;
    }
  }

  .dot {
    display: inline-block;
    width: 4px;
    height: 4px;
    border-radius: 2px;
    margin-right: 5px;
    background-color: $text-default;
    vertical-align: top;
    margin-top: 10px;
  }
}

@include desktop {
  .noticeBox {
    padding: 24px;
    border-radius: 16px;

    .contentTitle {
      font-size: 24px;
      line-height: 36px;
      margin-bottom: 16px;

      .noticeIcon {
        width: 20px;
        height: 20px;
        margin-top: 5px;
        margin-right: 5px;
      }
    }

    .content {
      font-size: 18px;
      line-height: 27px;
    }
  }
}

@include tablet {
  .noticeBox {
    padding: 24px;
    border-radius: 16px;

    .contentTitle {
      font-size: 24px;
      line-height: 36px;
      margin-bottom: 16px;

      .noticeIcon {
        width: 20px;
        height: 20px;
        margin-top: 5px;
        margin-right: 5px;
      }
    }

    .content {
      font-size: 18px;
      line-height: 27px;
    }
  }
}

@include mobile {
  .noticeBox {
    padding: 16px;
    border-radius: 8px;

    .contentTitle {
      font-size: 16px;
      line-height: 24px;
      margin-bottom: 8px;

      .noticeIcon {
        width: 16px;
        height: 16px;
        margin-right: 3px;
        margin-top: 3px;
      }
    }

    .content {
      font-size: 14px;
      line-height: 21px;
    }
  }
}
</style>
