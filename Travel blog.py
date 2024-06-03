import React from 'react';
import { AppBar, Toolbar, Typography, Container, Grid, Card, CardMedia, CardContent } from '@mui/material';
import { makeStyles } from '@mui/styles';

const useStyles = makeStyles((theme) => ({
  appBar: {
    marginBottom: theme.spacing(4),
  },
  cardMedia: {
    paddingTop: '56.25%', // 16:9 aspect ratio
  },
}));

const TravelBlog = () => {
  const classes = useStyles();

  return (
    <div>
      <AppBar position="static" className={classes.appBar}>
        <Toolbar>
          <Typography variant="h6" component="div">
            My Travel Blog
          </Typography>
        </Toolbar>
      </AppBar>
      <Container>
        <Grid container spacing={3}>
          <Grid item xs={12} sm={6} md={4}>
            <Card>
              <CardMedia
                className={classes.cardMedia}
                image="https://via.placeholder.com/300"
                title="Placeholder Image"
              />
              <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                  Destination 1
                </Typography>
                <Typography variant="body2" color="textSecondary" component="p">
                  Description of your experience at this destination.
                </Typography>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} sm={6} md={4}>
            <Card>
              <CardMedia
                className={classes.cardMedia}
                image="https://via.placeholder.com/300"
                title="Placeholder Image"
              />
              <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                  Destination 2
                </Typography>
                <Typography variant="body2" color="textSecondary" component="p">
                  Description of your experience at this destination.
                </Typography>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} sm={6} md={4}>
            <Card>
              <CardMedia
                className={classes.cardMedia}
                image="https://via.placeholder.com/300"
                title="Placeholder Image"
              />
              <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                  Destination 3
                </Typography>
                <Typography variant="body2" color="textSecondary" component="p">
                  Description of your experience at this destination.
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        </Grid>
      </Container>
    </div>
  );
};

export default TravelBlog;