// src/App.jsx
import { useState } from "react";
import { Drawer, Button, List, ListItem, ListItemText } from "@mui/material";
import "./App.css";

function App() {
  const [open, setOpen] = useState(false);

  const toggleDrawer = (isOpen) => (event) => {
    // Para evitar que o drawer feche ao apertar tab/shift
    if (
      event.type === "keydown" &&
      (event.key === "Tab" || event.key === "Shift")
    ) {
      return;
    }
    setOpen(isOpen);
  };

  const DrawerList = (
    <List>
      <ListItem button>
        <ListItemText primary="Dashboard" />
      </ListItem>
      <ListItem button>
        <ListItemText primary="Minhas Tarefas" />
      </ListItem>
      <ListItem button>
        <ListItemText primary="Criar Tarefa" />
      </ListItem>
    </List>
  );

  return (
    <>
      <Button variant="contained" onClick={toggleDrawer(true)}>
        Open drawer
      </Button>

      <Drawer anchor="left" open={open} onClose={toggleDrawer(false)}>
        {DrawerList}
      </Drawer>
    </>
  );
}

export default App;
