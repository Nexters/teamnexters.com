export const state = () => ({
  reviewLimit: 6,
});

export const getters = {
  showDetail: (state) => state.showDetail,
  reviewLimit: (state) => state.reviewLimit,
};

export const mutations = {
  reviewLimit(state, limit) {
    state.reviewLimit = limit;
  },
  init(state) {
    state.reviewLimit = 6;
  },
};

export const actions = {
  reviewLimit({ commit }, limit) {
    commit("reviewLimit", limit);
  },
  init({ commit }) {
    commit("init");
  },
};
