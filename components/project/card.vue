<template>
  <div class="container">
    <nuxt-link :to="`project/${project.idx}`">
      <img class="thumbnail" :src="project.thumbnail" />
      <p class="name">{{ project.app_name }}</p>
      <p class="time">{{ project.th }} | {{ project.year }}</p>
    </nuxt-link>
    <div class="links">
      <a
        v-for="(link, platform) in project.link"
        :key="platform"
        class="link-item"
        :href="link"
      >
        {{ platform }}
      </a>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "ProjectCard",
  props: {
    project: {
      type: Object,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
* {
  font-family: Spoqa Han Sans Neo;
}
.container {
  box-shadow: 0px 2px 32px rgba(0, 0, 0, 0.12);
}
.name {
  cursor: pointer;
}
a {
  text-decoration: none;
}
.links {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.link-item {
  font-weight: bold;
  font-size: 16px;
  line-height: 24px;
  text-align: center;
  letter-spacing: -0.02em;

  color: #000000;
  width: 100%;
  height: 45px;
  line-height: 45px;
  text-align: center;
  border: 1px solid #dddddd;
  border-radius: 8px;
  margin-right: 8px;
  cursor: pointer;
}
.link-item:last-child {
  margin: 0;
}
@include d-c3 {
  .thumbnail {
    width: 100%;
    height: 207px;
    border-top-left-radius: 16px;
    border-top-right-radius: 16px;
  }
  .name,
  .time {
    margin-left: 16px;
  }
  .links {
    margin: 0 16px 16px 16px;
  }

  .name {
    font-style: normal;
    font-weight: bold;
    font-size: 24px;
    line-height: 36px;
    letter-spacing: -0.02em;
    color: #000000;
  }
  .time {
    font-style: normal;
    font-weight: normal;
    font-size: 14px;
    line-height: 21px;
    color: #777777;
  }
  .links {
    padding-top: 24px;
  }
}

@include d-c2 {
  .project {
    flex-basis: 364.5px;
    .thumbnail {
      width: 100%;
      height: 205px;
      border-top-left-radius: 16px;
      border-top-right-radius: 16px;
    }
    .name,
    .time {
      margin-left: 16px;
    }
    .links {
      margin: 0 16px 16px 16px;
    }

    .name {
      font-style: normal;
      font-weight: bold;
      font-size: 24px;
      line-height: 36px;
      letter-spacing: -0.02em;
      color: #000000;
    }
    .time {
      font-style: normal;
      font-weight: normal;
      font-size: 14px;
      line-height: 21px;
      color: #777777;
    }
    .links {
      padding-top: 24px;
    }
  }
}

@include d-c1 {
  .thumbnail {
    width: 100%;
    height: 401px;
    border-top-left-radius: 16px;
    border-top-right-radius: 16px;
  }
  .name,
  .time {
    margin-left: 16px;
  }
  .links {
    margin: 0 16px 16px 16px;
  }
  .name {
    font-style: normal;
    font-weight: bold;
    font-size: 24px;
    line-height: 36px;
    letter-spacing: -0.02em;
    color: #000000;
  }
  .time {
    font-style: normal;
    font-weight: normal;
    font-size: 14px;
    line-height: 21px;
    color: #777777;
  }
  .links {
    padding-top: 24px;
  }
}

@include m-c2 {
  .thumbnail {
    width: 100%;
    height: 216px;
    border-top-left-radius: 16px;
    border-top-right-radius: 16px;
  }
  .name,
  .time {
    margin-left: 16px;
  }
  .links {
    margin: 0 16px 16px 16px;
  }
  .name {
    padding-top: 8px;
    font-style: normal;
    font-weight: bold;
    font-size: 16px;
    line-height: 24px;
    letter-spacing: -0.02em;
    color: #000000;
  }
  .time {
    padding-top: 8px;
    font-style: normal;
    font-weight: normal;
    font-size: 12px;
    line-height: 18px;
    color: #777777;
  }
  .links {
    padding-top: 16px;
  }
}

@include m-c1 {
  .thumbnail {
    width: 100%;
    height: 216px;
    border-top-left-radius: 16px;
    border-top-right-radius: 16px;
  }
  .name,
  .time {
    margin-left: 16px;
  }
  .links {
    margin: 0 16px 16px 16px;
  }
  .name {
    padding-top: 8px;
    font-style: normal;
    font-weight: bold;
    font-size: 16px;
    line-height: 24px;
    letter-spacing: -0.02em;
    color: #000000;
  }
  .time {
    padding-top: 8px;
    font-style: normal;
    font-weight: normal;
    font-size: 12px;
    line-height: 18px;
    color: #777777;
  }
  .links {
    padding-top: 16px;
  }
}
</style>
