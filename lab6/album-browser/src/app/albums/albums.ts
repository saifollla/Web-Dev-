import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { Album } from '../models/album.model';
import { AlbumService } from '../album';

@Component({
  selector: 'app-albums',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './albums.html',
  styleUrl: './albums.css'
})
export class AlbumsComponent implements OnInit {
  albums: Album[] = [];
  loading: boolean = true;

  constructor(private albumService: AlbumService) {}

  ngOnInit(): void {
    this.fetchAlbums();
  }

  fetchAlbums(): void {
    this.albumService.getAlbums().subscribe({
      next: (data) => {
        this.albums = data;
        this.loading = false;
      },
      error: (err) => {
        console.error('Error fetching albums:', err);
        this.loading = false;
      }
    });
  }

  deleteAlbum(id: number): void {
    this.albums = this.albums.filter(a => a.id !== id);

    this.albumService.deleteAlbum(id).subscribe(() => {
      console.log(`Album ${id} deleted on server`);
    });
  }
}
