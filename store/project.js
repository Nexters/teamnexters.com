export const state = () => ({
  showDetail: false,
  project: {},
  projectLimit: 6,
});

export const getters = {
  showDetail: (state) => state.showDetail,
  project: (state) => state.project,
  projectLimit: (state) => state.projectLimit,
};

export const mutations = {
  showDetail(state, project) {
    state.showDetail = true;
    state.project = project;
    // document.documentElement.style.getPropertyValue("--scroll-y");
    const { body } = document;
    body.style.overflowY = "hidden";
  },
  dismiss(state) {
    state.showDetail = false;
    state.project = {};
    // document.documentElement.style.getPropertyValue("--scroll-y");
    const { body } = document;
    body.style.overflowY = "";
  },
  projectLimit(state, limit) {
    state.projectLimit = limit;
  },
  init(state) {
    state.showDetail = false;
    state.project = {};
    state.projectLimit = 6;
  },
};

export const actions = {
  dismiss({ commit }) {
    commit("dismiss");
  },
  showDetail({ commit }, project) {
    commit("showDetail", project);
  },
  projectLimit({ commit }, limit) {
    commit("projectLimit", limit);
  },
  init({ commit }) {
    commit("init");
  },
};
