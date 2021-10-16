<template>
  <div class="project-card-component-container" @click="showDetail(project)">
    <nuxt-link :to="`project#${project.idx}`">
      <img class="thumbnail" :src="thumbnail" />
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
      return this.project.thumbnail || require("~/assets/img/no-image.png");
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
  border: solid 1px $grey02;
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

  color: $black;
  width: 100%;
  height: 45px;
  line-height: 45px;
  text-align: center;
  border: 1px solid $grey02;
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
    color: $black;
  }
  .time {
    font-style: normal;
    font-weight: normal;
    font-size: 14px;
    line-height: 21px;
    color: $grey03;
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
      color: $black;
    }
    .time {
      font-style: normal;
      font-weight: normal;
      font-size: 14px;
      line-height: 21px;
      color: $grey03;
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
    color: $black;
  }
  .time {
    font-style: normal;
    font-weight: normal;
    font-size: 14px;
    line-height: 21px;
    color: $grey03;
  }
  .links {
    padding-top: 24px;
  }
}

@include m-c2 {
  .thumbnail {
    width: 100%;
    height: 216px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
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
    color: $black;
  }
  .time {
    padding-top: 8px;
    font-style: normal;
    font-weight: normal;
    font-size: 12px;
    line-height: 18px;
    color: $grey03;
  }
  .links {
    padding-top: 16px;
  }
}

@include m-c1 {
  .thumbnail {
    width: 100%;
    height: 216px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
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
    color: $black;
  }
  .time {
    padding-top: 8px;
    font-style: normal;
    font-weight: normal;
    font-size: 12px;
    line-height: 18px;
    color: $grey03;
  }
  .links {
    padding-top: 16px;
  }
}
</style>
