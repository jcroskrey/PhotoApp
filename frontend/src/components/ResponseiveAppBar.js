import React from "react";
import {
    AppBar,
    Toolbar,
    Box,
    Container,
    Avatar,
    Button,

  } from "@material-ui/core";
import '../../static/css/navbar.css';

const pages = ['Resume', 'Photography'];

function ResponsiveAppBar() {
  return (
    <>
    <AppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
      
          <Box sx={{flexGrow: 0, marginRight: 10}}>
            <Avatar 
                src="/static/images/D730220B-77B9-4AC9-8DA8-F7D5F3B6653C_1_100_o.jpeg"
                sx={{
                  height: 64,
                }}
                alt="profile"
            />
          </Box>

          <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
            {pages.map((page) => (
              <Button
                key={page}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                {page}
              </Button>
            ))}
          </Box>

        </Toolbar>
      </Container>
    </AppBar>
    </>
  )
}
export default ResponsiveAppBar;
