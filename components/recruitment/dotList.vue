<template>
  <article class="dotListArea">
    <h2 class="dotListTitle">{{ dotListTitle }}</h2>
    <pre v-for="item in items" :key="item.id" class="dotItem">
      <span>{{ item.text }}</span>
    </pre>
  </article>
</template>

<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "Qualification",
  props: {
    dotListTitle: {
      type: String,
      require: true,
    },
    items: {
      type: Array,
      require: false,
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

.dotListArea {
  .dotListTitle {
    font-weight: 700;
  }

  .dotItem {
    display: flex;
    font-weight: 400;
    white-space: pre-line;

    &::before {
      display: inline-block;
      content: "";
      vertical-align: top;
      height: 4px;
      width: 4px;
      background-color: $text-default;
      border-radius: 2px;
      margin-right: 5px;
      flex: none;
    }
  }
}

@include desktop {
  .dotListArea {
    .dotListTitle {
      font-size: 32px;
      line-height: 48px;
    }

    .dotItem {
      font-size: 24px;
      line-height: 36px;
      margin-top: 16px;

      &::before {
        margin-top: 14px;
      }
    }
  }
}

@include tablet {
  .dotListArea {
    .dotListTitle {
      font-size: 32px;
      line-height: 48px;
    }

    .dotItem {
      font-size: 24px;
      line-height: 36px;
      margin-top: 16px;

      &::before {
        margin-top: 14px;
      }
    }
  }
}

@include mobile {
  .dotListArea {
    .dotListTitle {
      font-size: 24px;
      line-height: 36px;
    }

    .dotItem {
      font-size: 16px;
      line-height: 24px;
      margin-top: 8px;

      &::before {
        margin-top: 8px;
      }
    }
  }
}
</style>
