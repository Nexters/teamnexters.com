<template>
  <footer>
    <div class="footer">
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
      <div class="copyrights">
        {{ copyrights }}
      </div>
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
@import "~/assets/css/_device.scss";

footer {
  margin-top: auto;
}

.footer {
  @include mobile {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0 0 24px 24px;
    .sns {
      display: flex;
      margin-right: auto;
      img {
        height: 24px;
        width: 24px;
      }
      ul {
        flex-direction: column;
        margin-right: 16px;
      }
    }
    .copyrights {
      margin-right: auto;
      padding-top: 16px;

      font-style: normal;
      font-weight: normal;
      font-size: 14px;
      line-height: 21px;
      text-align: center;
      letter-spacing: -0.02em;
    }
  }
  @include tablet {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0 0 24px 24px;
    .sns {
      display: flex;
      margin-right: auto;
      img {
        height: 24px;
        width: 24px;
      }
      ul {
        flex-direction: column;
        margin-right: 16px;
      }
    }
    .copyrights {
      margin-right: auto;
      padding-top: 16px;

      font-style: normal;
      font-weight: normal;
      font-size: 14px;
      line-height: 21px;
      text-align: center;
      letter-spacing: -0.02em;
    }
  }
  @include desktop {
    display: flex;
    align-items: center;
    padding-left: 64px;
    width: 1200px;
    margin: auto auto 32px auto;

    .sns {
      display: flex;
      img {
        height: 32px;
        width: 32px;
      }
      ul {
        flex-direction: column;
        margin-right: 32px;
      }
    }
    .copyrights {
      margin-left: auto;
      padding-right: 64px;

      font-style: normal;
      font-weight: normal;
      font-size: 16px;
      line-height: 24px;
      text-align: center;
      letter-spacing: -0.02em;
    }
  }
}
</style>
