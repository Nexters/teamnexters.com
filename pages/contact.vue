<template>
  <div class="contactBody">
    <div class="headerArea">
      <h1 class="header">Contact Us</h1>
    </div>
    <article class="contactArea" @keydown="debug">
      <ContactBox class="contactBox" :contactType="`kakao`" />
      <ContactBox class="contactBox" :contactType="`gmail`" />
      <ContactBox class="contactBox" :contactType="`facebook`" />
    </article>
    <div class="headerArea">
      <h1 class="header">FAQ</h1>
    </div>
    <article class="faqArea">
      <ContactFaqBox
        v-for="faq in faqs"
        :key="faq.idx"
        class="faqBox"
        :question="faq.question"
        :answer="faq.answer"
      />
    </article>
  </div>
</template>

<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "Contact",
  fetchOnServer: false,
  setup() {},
  data() {
    return {
      faqs: [],
    };
  },
  async fetch() {
    const [_, ...rawdata] = await this.FetchAll();
    this.faqs = rawdata.map((faq, index) => ({
      idx: index,
      question: faq[0],
      answer: faq[1],
    }));
  },
  methods: {
    debug(e) {
      console.log(e);
    },
    FetchAll: async function () {
      const { results } = await this.$content("contact").fetch();
      const { rawData } = results[0].result;

      return rawData;
    },
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
* {
  font-family: Spoqa Han Sans Neo;
}

.contactBody {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  align-items: center;

  .headerArea {
    width: 100%;

    .header {
      font-weight: 700;
    }
  }

  .contactArea,
  .faqArea {
    width: 100%;
  }
}

@include d-c3 {
  .contactBody {
    padding: 64px;

    .headerArea {
      max-width: 1200px;
      margin-bottom: 32px;
      font-size: 60px;
      line-height: 90px;
    }

    .contactArea {
      max-width: 1200px;
      margin-bottom: 120px;

      .contactBox {
        margin-bottom: 16px;
      }
    }

    .faqArea {
      max-width: 1200px;

      .faqBox {
        margin-bottom: 16px;
      }
    }
  }
}

@include d-c2 {
  .contactBody {
    padding: 64px;

    .headerArea {
      max-width: 1200px;
      margin-bottom: 32px;
      font-size: 60px;
      line-height: 90px;
    }

    .contactArea {
      max-width: 1200px;
      margin-bottom: 120px;

      .contactBox {
        margin-bottom: 16px;
      }
    }

    .faqArea {
      max-width: 1200px;

      .faqBox {
        margin-bottom: 16px;
      }
    }
  }
}

@include d-c1 {
  .contactBody {
    padding: 64px;

    .headerArea {
      max-width: 1200px;
      margin-bottom: 32px;
      font-size: 60px;
      line-height: 90px;
    }

    .contactArea {
      max-width: 1200px;
      margin-bottom: 120px;

      .contactBox {
        margin-bottom: 16px;
      }
    }

    .faqArea {
      max-width: 1200px;

      .faqBox {
        margin-bottom: 16px;
      }
    }
  }
}

@include m-c2 {
  .contactBody {
    padding: 32px;

    .headerArea {
      max-width: 713px;
      margin-bottom: 16px;
      font-size: 32px;
      line-height: 48px;
    }

    .contactArea {
      max-width: 713px;
      margin-bottom: 64px;

      .contactBox {
        margin-bottom: 8px;
      }
    }

    .faqArea {
      max-width: 713px;

      .faqBox {
        margin-bottom: 8px;
      }
    }
  }
}

@include m-c1 {
  .contactBody {
    padding: 32px;

    .headerArea {
      max-width: 713px;
      margin-bottom: 16px;
      font-size: 32px;
      line-height: 48px;
    }

    .contactArea {
      max-width: 713px;
      margin-bottom: 64px;

      .contactBox {
        margin-bottom: 8px;
      }
    }

    .faqArea {
      max-width: 713px;

      .faqBox {
        margin-bottom: 8px;
      }
    }
  }
}
</style>
