<template>
  <article class="faqBox">
    <section class="questionArea" @click="isOpen = !isOpen">
      <p>{{ question }}</p>
      <img class="icon" :src="imageResource" />
    </section>
    <section v-if="isOpen" class="answerArea">
      <p>{{ answer }}</p>
    </section>
  </article>
</template>

<script>
import { defineComponent } from "@nuxtjs/composition-api";

export default defineComponent({
  name: "FaqBox",
  props: {
    question: {
      type: String,
      require: true,
    },
    answer: {
      type: String,
      require: true,
    },
  },
  data() {
    return {
      isOpen: false,
    };
  },
  computed: {
    imageResource: {
      get() {
        return this.isOpen
          ? require("~/assets/img/arrow_up.svg")
          : require("~/assets/img/arrow_down.svg");
      },
      set(value) {
        this.isOpen = value;
      },
    },
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
@import "~/assets/css/setting.scss";

.faqBox {
  width: 100%;
  display: flex;
  flex-direction: column;
  background-color: $background-sub;
  border-radius: 16px;

  .questionArea {
    width: 100%;
    display: flex;
    justify-content: space-between;
    font-weight: 700;

    &:hover {
      cursor: pointer;
    }
  }

  .answerArea {
    font-weight: 400;
    white-space: pre-wrap;
  }

  .icon {
    align-self: center;
  }
}

@include d-c3 {
  .faqBox {
    padding: 32px;
    box-sizing: border-box;
  }

  .questionArea {
    font-size: 24px;
    line-height: 36px;
  }

  .answerArea {
    font-size: 18px;
    line-height: 27px;
    margin-top: 24px;
  }

  .icon {
    width: 24px;
    height: 24px;
    margin-left: 24px;
  }
}

@include d-c2 {
  .faqBox {
    padding: 32px;
    box-sizing: border-box;
  }

  .questionArea {
    font-size: 24px;
    line-height: 36px;
  }

  .answerArea {
    font-size: 18px;
    line-height: 27px;
    margin-top: 24px;
  }

  .icon {
    width: 24px;
    height: 24px;
    margin-left: 24px;
  }
}

@include d-c1 {
  .faqBox {
    padding: 32px;
    box-sizing: border-box;
  }

  .questionArea {
    font-size: 16px;
    line-height: 24px;
  }

  .answerArea {
    font-size: 18px;
    line-height: 27px;
    margin-top: 24px;
  }

  .icon {
    width: 24px;
    height: 24px;
    margin-left: 24px;
  }
}

@include m-c2 {
  .faqBox {
    padding: 24px;
    border-radius: 8px;
  }

  .questionArea {
    font-size: 16px;
    line-height: 24px;
  }

  .answerArea {
    font-size: 14px;
    line-height: 21px;
    margin-top: 16px;
  }

  .icon {
    width: 16px;
    height: 16px;
    margin-left: 16px;
  }
}

@include m-c1 {
  .faqBox {
    padding: 24px;
    border-radius: 8px;
  }

  .questionArea {
    font-size: 16px;
    line-height: 24px;
  }

  .answerArea {
    font-size: 14px;
    line-height: 21px;
    margin-top: 16px;
  }

  .icon {
    width: 16px;
    height: 16px;
    margin-left: 16px;
  }
}
</style>
