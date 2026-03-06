import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Album } from '../models/album.model';
import { AlbumService } from '../album';

@Component({
  selector: 'app-album-detail',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './album-detail.html',
  styleUrl: './album-detail.css'
})
export class AlbumDetailComponent implements OnInit {
  album!: Album;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private albumService: AlbumService
  ) {}

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));

    this.albumService.getAlbum(id).subscribe((album) => {
      this.album = album;
    });
  }

  save(): void {
    this.albumService.updateAlbum(this.album).subscribe((updated) => {
      alert('Changes saved successfully!');
      console.log('Updated album:', updated);
    });
  }

  goBack(): void {
    this.router.navigate(['/albums']);
  }
}
