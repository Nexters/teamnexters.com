export const state = () => ({
  showDetail: false,
  project: {},
});

export const getters = {
  showDetail: (state) => state.showDetail,
  project: (state) => state.project,
};

export const mutations = {
  showDetail(state, project) {
    state.showDetail = true;
    state.project = project;
    document.documentElement.style.getPropertyValue("--scroll-y");
    const { body } = document;
    body.style.overflowY = "hidden";
  },
  dismiss(state) {
    state.showDetail = false;
    state.project = {};
    document.documentElement.style.getPropertyValue("--scroll-y");
    const { body } = document;
    body.style.overflowY = "";
  },
  init(state) {
    state.showDetail = false;
    state.project = {};
  },
};

export const actions = {
  dismiss({ commit }) {
    commit("dismiss");
  },
  showDetail({ commit }, project) {
    commit("showDetail", project);
  },
  init({ commit }) {
    commit("init");
  },
};
