<template>
  <div class="noticeBox">
    <h1 class="contentTitle">{{ boxTitle }}</h1>
    <p v-for="content in contents" :key="content.id" class="content">
      - {{ content.text }}
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
  background-color: $grey01;
  border: 1px solid $grey02;
  border-radius: 16px;

  .contentTitle {
    font-style: bold;
  }
}

@include desktop {
  .noticeBox {
    padding: 24px;

    .contentTitle {
      font-size: 24px;
      line-height: 36px;
      margin-bottom: 16px;
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

    .contentTitle {
      font-size: 24px;
      line-height: 36px;
      margin-bottom: 16px;
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

    .contentTitle {
      font-size: 16px;
      line-height: 24px;
      margin-bottom: 8px;
    }

    .content {
      font-size: 14px;
      line-height: 21px;
    }
  }
}
</style>
