<template>
  <div class="project-card-component-container" @click="showDetail(project)">
    <nuxt-link :to="`project#${project.idx}`">
      <img class="thumbnail" :src="thumbnail" />
      <p class="name">{{ project.app_name }}</p>
      <p class="time">{{ project.th }}th | {{ project.year }}</p>
    </nuxt-link>
    <div class="links">
      <div
        v-for="(link, platform) in project.link"
        :key="platform"
        class="link-item"
      >
        <a :href="link" @click.stop="">
          {{ platform }}
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "@nuxtjs/composition-api";
import { mapActions } from "vuex";
const ProjectCard = defineComponent({
  name: "ProjectCard",
  props: {
    project: {
      type: Object,
      required: true,
    },
  },
  computed: {
    thumbnail() {
      return this.project.thumbnail || require("~/assets/img/no_image.png");
    },
  },
  methods: {
    ...mapActions({ showDetail: "project/showDetail" }),
  },
});

export default ProjectCard;
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
@import "~/assets/css/setting.scss";

* {
  font-family: Spoqa Han Sans Neo;
}
.project-card-component-container {
  display: flex;
  flex-direction: column;
  border: solid 1px $grey02;

  .links {
    margin: auto 0 0;
  }
}

.name {
  cursor: pointer;
}
a {
  text-decoration: none;
}

@include d-c3 {
  .thumbnail {
    width: 100%;
    height: 207px;
    border-top-left-radius: 16px;
    border-top-right-radius: 16px;
  }

  .name {
    margin: 24px 0 0 24px;
    font-style: normal;
    font-weight: bold;
    font-size: 24px;
    line-height: 36px;
    letter-spacing: -0.02em;
    color: $black;
  }
  .time {
    margin: 8px 0 0 24px;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 27px;
    color: $grey03;
  }

  .links {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 24px;
    grid-gap: 8px;
    .link-item {
      a {
        font-weight: bold;
        font-size: 18px;
        line-height: 27px;
        text-align: center;
        letter-spacing: -0.02em;
        color: $black;
      }
      padding: 16px 24px;
      width: 100%;
      text-align: center;
      border-radius: 8px;
      border: 1px solid $grey02;
      cursor: pointer;
    }
    .link-item:last-child {
      a {
        margin: 0;
      }
    }
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

    .name {
      margin: 24px 0 0 24px;
      font-style: normal;
      font-weight: bold;
      font-size: 24px;
      line-height: 36px;
      letter-spacing: -0.02em;
      color: $black;
    }
    .time {
      margin: 8px 0 0 24px;
      font-style: normal;
      font-weight: normal;
      font-size: 18px;
      line-height: 27px;
      color: $grey03;
    }
    .links {
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      padding: 24px;
      grid-gap: 8px;
      .link-item {
        a {
          font-weight: bold;
          font-size: 18px;
          line-height: 27px;
          text-align: center;
          letter-spacing: -0.02em;
          color: $black;
        }
        padding: 16px 24px;
        width: 100%;
        text-align: center;
        border-radius: 8px;
        border: 1px solid $grey02;
        cursor: pointer;
      }
      .link-item:last-child {
        a {
          margin: 0;
        }
      }
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
  .name {
    margin: 24px 0 0 24px;
    font-style: normal;
    font-weight: bold;
    font-size: 24px;
    line-height: 36px;
    letter-spacing: -0.02em;
    color: $black;
  }
  .time {
    margin: 8px 0 0 24px;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 27px;
    color: $grey03;
  }
  .links {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 24px;
    grid-gap: 8px;
    .link-item {
      a {
        font-weight: bold;
        font-size: 18px;
        line-height: 27px;
        text-align: center;
        letter-spacing: -0.02em;
        color: $black;
      }
      padding: 16px 24px;
      width: 100%;
      text-align: center;
      border-radius: 8px;
      border: 1px solid $grey02;
      cursor: pointer;
    }
    .link-item:last-child {
      a {
        margin: 0;
      }
    }
  }
}

@include m-c2 {
  .thumbnail {
    width: 100%;
    height: 216px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
  }
  .name {
    margin: 16px 0 0 16px;
    font-style: normal;
    font-weight: bold;
    font-size: 16px;
    line-height: 24px;
    letter-spacing: -0.02em;
    color: $black;
  }
  .time {
    margin: 8px 0 0 16px;
    font-style: normal;
    font-weight: normal;
    font-size: 14px;
    line-height: 21px;
    color: $grey03;
  }
  .links {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 16px;
    grid-gap: 8px;
    .link-item {
      a {
        font-weight: bold;
        font-size: 14px;
        line-height: 21px;
        text-align: center;
        letter-spacing: -0.02em;
        color: $black;
      }
      padding: 12px 0 12px 0;
      width: 100%;
      text-align: center;
      border-radius: 4px;
      border: 1px solid $grey02;
      cursor: pointer;
    }
    .link-item:last-child {
      a {
        margin: 0;
      }
    }
  }
}

@include m-c1 {
  .thumbnail {
    width: 100%;
    height: 216px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
  }
  .name {
    margin: 16px 0 0 16px;
    font-style: normal;
    font-weight: bold;
    font-size: 16px;
    line-height: 24px;
    letter-spacing: -0.02em;
    color: $black;
  }
  .time {
    margin: 8px 0 0 16px;
    font-style: normal;
    font-weight: normal;
    font-size: 14px;
    line-height: 21px;
    color: $grey03;
  }
  .links {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 16px;
    grid-gap: 8px;
    .link-item {
      a {
        font-weight: bold;
        font-size: 14px;
        line-height: 21px;
        text-align: center;
        letter-spacing: -0.02em;
        color: $black;
      }
      padding: 12px 0 12px 0;
      width: 100%;
      text-align: center;
      border-radius: 4px;
      border: 1px solid $grey02;
      cursor: pointer;
    }
    .link-item:last-child {
      a {
        margin: 0;
      }
    }
  }
}
</style>
