<template>
  <footer>
    <div class="sns">
      <ul v-for="item in items" :key="item.name">
        <a :href="item.href">
          <img
            :src="require(`~/assets/img/${item.name}.png`)"
            :alt="item.name"
          />
        </a>
      </ul>
    </div>
    <div>
      {{ copyrights }}
    </div>
  </footer>
</template>

<script lang="ts">
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "Footer",
  props: {
    items: {
      type: Array,
      required: true,
    },
    copyrights: {
      type: String,
      required: true,
    },
  },
  setup() {
    return {};
  },
});
</script>

<style lang="scss" scoped>
footer {
  margin-top: auto;
  margin-left: 10%;
  margin-bottom: 32px;
  display: flex;
  align-items: center;
  img {
    height: 32px;
    width: 32px;
  }
  .sns {
    display: flex;
    ul {
      flex-direction: column;
      margin-right: 32px;
    }
  }
  .copyrights-mobile {
    margin-left: auto;
    margin-left: 24px;
  }
  .copyrights-pc {
    margin-right: 64px;
  }
}
</style>
