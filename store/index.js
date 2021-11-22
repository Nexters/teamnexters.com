export const state = () => ({
  isMenuOpen: false,
});

export const getters = {
  isMenuOpen: (state) => state.isMenuOpen,
};

export const mutations = {
  toggleMenu(state) {
    if (state.isMenuOpen) {
      document.documentElement.style.getPropertyValue("--scroll-y");
      const { body } = document;
      body.style.overflowY = "";
    } else {
      document.documentElement.style.getPropertyValue("--scroll-y");
      const { body } = document;
      body.style.overflowY = "hidden";
    }
    state.isMenuOpen = !state.isMenuOpen;
  },
  init(state) {
    state.isMenuOpen = false;
    document.documentElement.style.getPropertyValue("--scroll-y");
    const { body } = document;
    body.style.overflowY = "";
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
