{
  const rand = {
    "noise": function () {
      const SIGN = Math.random() < Math.random() ? -1 : 1;
      return Math.floor(Math.random() + SIGN * Math.random());
    },
    "sign": function () {
      const tmp = [-1, -1, -1, -1, -1, -1, +1, -1, -1, -1];
      const index = Math.floor(Math.random() * tmp.length);
      return tmp[index];
    }
  };
  //
  Object.defineProperty(HTMLElement.prototype, "offsetHeight", {
    "get": new Proxy(Object.getOwnPropertyDescriptor(HTMLElement.prototype, "offsetHeight").get, {
      apply(target, self, args) {
        try {
          const height = Math.floor(self.getBoundingClientRect().height);
          const valid = height && rand.sign() === 1;
          const result = valid ? height + rand.noise() : height;
          //
          if (valid && result !== height) {
            window.top.postMessage("font-defender-alert", '*');
          }
          //
          return result;
        } catch (e) {
          //return Reflect.apply(target, self, args);
        }
      }
    })
  });
  //
  Object.defineProperty(HTMLElement.prototype, "offsetWidth", {
    "get": new Proxy(Object.getOwnPropertyDescriptor(HTMLElement.prototype, "offsetWidth").get, {
      apply(target, self, args) {
        const width = Math.floor(self.getBoundingClientRect().width);
        const valid = width && rand.sign() === 1;
        const result = valid ? width + rand.noise() : width;
        //
        if (valid && result !== width) {
          window.top.postMessage("font-defender-alert", '*');
        }
        //
        return result;
      }
    })
  });
}

{
  const mkey = "font-defender-sandboxed-frame";
  document.documentElement.setAttribute(mkey, '');
  //
  window.addEventListener("message", function (e) {
    if (e.data && e.data === mkey) {
      e.preventDefault();
      e.stopPropagation();
      //
      if (e.source) {
        if (e.source.HTMLElement) {
          Object.defineProperty(e.source.HTMLElement.prototype, "offsetWidth", {
            "get": Object.getOwnPropertyDescriptor(HTMLElement.prototype, "offsetWidth").get
          });
          //
          Object.defineProperty(e.source.HTMLElement.prototype, "offsetHeight", {
            "get": Object.getOwnPropertyDescriptor(HTMLElement.prototype, "offsetHeight").get
          });
        }
      }
    }
  }, false);
}