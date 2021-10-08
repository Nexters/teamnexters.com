export const state = () => ({
  isMenuOpen: false,
});

export const getters = {
  isMenuOpen: (state) => state.isMenuOpen,
};

export const mutations = {
  toggleMenu(state) {
    state.isMenuOpen = !state.isMenuOpen;
  },
  init(state) {
    state.isMenuOpen = false;
  },
};

export const actions = {
  toggleMenu({ commit }) {
    commit("toggleMenu");
  },
  init({ commit }) {
    commit("init");
  },
};
