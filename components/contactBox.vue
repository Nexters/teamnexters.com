<template>
  <div class="contactBox">
    <IconBase imageName="kakao_16" />
  </div>
</template>

<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "ContactBox",
  props: {
    icon: {
      type: String,
      require: false,
    },
    key: {
      type: String,
      require: true,
    },
    value: {
      type: String,
      require: true,
    },
  },
});
</script>

<style scoped></style>
