export const state = () => ({
  reviews: [],
  reviewLimit: 6,
});

export const getters = {
  showDetail: (state) => state.showDetail,
  reviews: (state) => state.reviews,
  reviewLimit: (state) => state.reviewLimit,
};

export const mutations = {
  reviewLimit(state, limit) {
    state.reviewLimit = limit;
  },
  init(state) {
    state.reviews = [];
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
