<template>
  <transition name="contact" mode="out-in">
    <div class="contactBody">
      <div class="headerArea">
        <h2 class="header">Contact Us</h2>
      </div>
      <article class="contactArea" @keydown="debug">
        <ContactBox
          class="contactBox"
          :contact-type="`kakao`"
          :on-click="handleClick('kakao')"
        />
        <ContactBox
          class="contactBox"
          :contact-type="`gmail`"
          :on-click="handleClick('gmail')"
        />
        <ContactBox
          class="contactBox"
          :contact-type="`facebook`"
          :on-click="handleClick('facebook')"
        />
      </article>
      <div id="faq" class="headerArea">
        <h2 class="header">FAQ</h2>
      </div>
      <article class="faqArea">
        <FaqBox
          v-for="faq in faqs"
          :key="faq.idx"
          class="faqBox"
          :question="faq.question"
          :answer="faq.answer"
        />
      </article>
    </div>
  </transition>
</template>

<script>
import { defineComponent } from "@nuxtjs/composition-api";

export default defineComponent({
  name: "Contact",
  transition: {
    name: "contact",
  },
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
  mounted() {
    const faq = this.$route.hash || null;

    if (faq === "#faq") {
      setTimeout(() => {
        const scroll = document.getElementById("faq");
        window.scrollTo({ top: scroll.offsetTop, left: 0, behavior: "smooth" });
      }, 300);
    }
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
    handleClick: (action) => () => {
      switch (action) {
        case "kakao": {
          window.location.href = "https://pf.kakao.com/_xdxmnnj";
          break;
        }
        case "facebook": {
          window.location.href = "https://www.facebook.com/Nexterspage";
          break;
        }
        case "gmail": {
          const textarea = document.createElement("textarea");
          document.body.appendChild(textarea);
          textarea.value = "teamnexters@gmail.com";
          textarea.select();
          document.execCommand("copy");
          document.body.removeChild(textarea);
          alert("'teamnexters@gmail.com' 메일 주소를 복사했습니다. ");
          break;
        }
      }
      return;
    },
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
* {
  font-family: Spoqa Han Sans Neo;
}

.contact-enter-active,
.contact-leave-active {
  transition: opacity 1.5s;
}
.contact-enter,
.contact-leave-active {
  opacity: 0;
}

.contactBody {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  align-items: center;
  margin-top: 73px;

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
      font-size: 48px;
      line-height: 64px;
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
      font-size: 48px;
      line-height: 64px;
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
      font-size: 48px;
      line-height: 64px;
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
