import { Link as RouterLink, NavLink } from 'react-router-dom';
import { AppBar, Avatar, Box, Link, Toolbar } from '@material-ui/core';
import { Logo } from './logo';


import DownloadIcon from '@material-ui/icons/PictureAsPdf';

export const Navbar = () => (
  <AppBar
    elevation={0}

    sx={{ backgroundColor: '#1e212a' }}
  >
    <Toolbar
      disableGutters
      sx={{
        alignItems: 'center',
        display: 'flex',
        minHeight: 64,
        justifyContent :'space-between',
        px: 3,
        py: 1,
        mr:5
      }}
    >
      <Box
        component={RouterLink}
        to="/"
        sx={{
          alignItems: 'center',
          display: 'flex',
          justifyContent: 'center'
        }}
      >
       <Logo /></Box> 
       <Box >
         <a style={{color:'white'}} download href='/static/Khiati-Hamroun-Master-2021.pdf' >   
      
       <Box sx={{
        alignItems: 'center',
        display: 'flex'
      }}><DownloadIcon/><Box> Our paper | Time series forecasting </Box></Box>  
         </a>
      </Box>

     
    </Toolbar>
  </AppBar>
);
