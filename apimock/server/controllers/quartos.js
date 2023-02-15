const data = require("../data");
const accounts = require("./accounts");

function getMaxId(items) {
  return Math.max(...items.map((item) => item.id));
}

module.exports = {
  find: (req, res) => {
    const { id } = req.params;
    if (id != undefined) {
      const quarto = data.quartos.find((t) => t.id == id);
      if (!quarto|| quarto.userId != loggedUser.id) {
        res.status(404).end();
        return;
      }
      res.send(quarto);
      return;
    }
    const response = {
      todos: data.quartos.filter((t) => t.userId == loggedUser.id),
    };
    res.send(response);
  },
  add: (req, res) => {
    const loggedUser = accounts.loginRequired(req, res);
    if (!loggedUser) {
      return;
    }
    const { description } = req.body;
    const { nome } = req.body;
    const { cidade } = req.body;
    const { valor } = req.body;
    const { imagem } = req.body;

    const id = getMaxId(data.quartos) + 1;
    const newQuarto = {
      id,
      description,
      nome,
      cidade,
      valor,
      imagem,
      userId: loggedUser.id,
    };
    data.quartos.push(newQuarto);
    res.send(newQuarto);
  },
};
