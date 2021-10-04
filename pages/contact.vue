<template>
  <div class="contactBody" @keydown="debug">
    <ContactBox class="contactBox" :contactType="`kakao`" />
    <ContactBox class="contactBox" :contactType="`gmail`" />
    <ContactBox class="contactBox" :contactType="`facebook`" />
  </div>
</template>

<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "Contact",
  fetchOnServer: false,
  setup() {},
  data() {
    return {};
  },
  async fetch() {},
  methods: {
    debug(e) {
      console.log(e);
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
}

@include d-c3 {
  .contactBody {
    padding: 64px;

    .contactBox {
      max-width: 1200px;
      margin-bottom: 16px;
    }
  }
}

@include d-c2 {
  .contactBody {
    padding: 64px;

    .contactBox {
      max-width: 1200px;
      margin-bottom: 16px;
    }
  }
}

@include d-c1 {
  .contactBody {
    padding: 64px;

    .contactBox {
      max-width: 1200px;
      margin-bottom: 16px;
    }
  }
}

@include m-c2 {
  .contactBody {
    padding: 32px;

    .contactBox {
      max-width: 713px;
      margin-bottom: 8px;
    }
  }
}

@include m-c1 {
  .contactBody {
    padding: 32px;

    .contactBox {
      max-width: 713px;
      margin-bottom: 8px;
    }
  }
}
</style>
